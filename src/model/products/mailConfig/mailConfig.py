# ======== Import Libraries ===========
from cryptography.fernet import Fernet
from src.services.sql.queryExecute import dataFetch
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib
from datetime import datetime, timedelta
import secrets
from sqlalchemy import text
# ======== Import Dto, Entity ===========
from src.model.entity.login.login import UsersLoginInformation
from src.model.entity.myUnimo.myUnimo import MyUnimoClientDetails
from src.model.entity.mailConfig.mailConfig import MailConfigureInfo
from src.model.dto.mailConfig.mailConfig import MailConfigureDto, MailConfigureWithDto
from src.model.products.errorLog.errorLog import *

mailConfigureDto = MailConfigureDto()
mailConfigureWithDto = MailConfigureWithDto()
mailConfigureWithDtoList = MailConfigureWithDto(many=True)


def mailConfigurationSave(data):
    try:
        print('mailConfigurationSave')
        # Password Encryption Key Generated
        key = Fernet.generate_key()
        key = str(key)[2:-1]
        # print('c', key)

        cipher_suite = Fernet(key)
        # print('c', cipher_suite)

        # Password Encryption Generated
        encrypted_password = cipher_suite.encrypt(data['password'].encode()).decode()

        mailConfigSave = MailConfigureInfo(
            isActive=data['isActive'],
            senderEmail=data['senderEmail'],
            password=str(encrypted_password),
            subject=data['subject'],
            body=data['body'] if 'body' in data else None,
            signature=data['signature'],
            port=data['port'],
            server=data['server'],
            mailFor=data['mailFor'],
            key=str(key),
            senderTitle=data['senderTitle'],
            createdBy=data['createdBy'] if 'createdBy' in data else None
        )
        db.session.add(mailConfigSave)
        db.session.commit()
        result = mailConfigureDto.dump(mailConfigSave)
        print('mail config save', result['id'])

        return "Mail configuration save successfully"

    except Exception as e:
        print('Save Mail Config Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/mail/saveMailConfig'
        function = 'mailConfigurationSave'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return "Mail configuration saved failed"
        else:
            return "Mail configuration saved failed. Error Log Save Failed"


def getActiveMailConfiguration(mailFor):
    try:
        print('getActiveMailConfiguration')

        and_clause = ["%s = '%s'" % ('mail_for', mailFor), "%s = %s" % ('is_active', True)]
        tableDetails = ("sender_email, password, key, subject, body, signature, port, "
                        "server, sender_title from mail_configuration")
        and_clause_str = ' AND '.join(and_clause)
        sql_query = 'select ' + tableDetails + ' where ' + and_clause_str
        mailData = dataFetch(sql_query, 'one')
        return mailData

    except Exception as e:
        print('', e)

        errorMessage = f'{e}'
        url = '/api/v1/mail/getActiveMailConfig'
        function = 'getActiveMailConfiguration'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return "Mail configuration Saved Failed"
        else:
            return "Mail configuration Saved Failed. Error Log Save Failed"


def sendRegistrationVerification(email):
    try:
        print('send Registration Verification')
        token = secrets.token_urlsafe(16)
        expiration_time = datetime.utcnow() + timedelta(hours=6)

        verification_url = f'http://localhost:3000/pages/verify?email={email}&token={token}'
        body = f'Click the following link to verify your email: {verification_url}'
        print('send Registration Verification')

        connection = db.engine.connect()
        try:
            sql = text("""update users_login set expiration_time=:expiration_time, token=:token where email=:email""")
            connection.execute(sql, {"token": token, "expiration_time": expiration_time, "email": email})
            connection.commit()  # Manually commit the transaction
        except Exception as e:
            print(f"An error occurred: {e}")
            connection.rollback()
        finally:
            connection.close()

        return mailSend(email, body, 'Registration', '', '')

    except Exception as e:
        print('Email Send Exception', e)

        errorMessage = f'{e}'
        url = '/api/v1/mail/confirmationSend'
        function = 'sendRegistrationVerification'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return "Mail send failed"
        else:
            return "Mail send failed. Error Log Save Failed"


def sendInvitation(email, id, serviceName, meetingLink):
    try:
        print('send Registration Verification')
        token = secrets.token_urlsafe(32)

        verification_url = f'http://localhost:3000/register/?token={token}&type=Immigrant'
        body = (f'You have received a request for {serviceName} Services. Would you like to accept the request the '
                f'request?: {verification_url}'
                f'For Discovery Call Meeting Link ~ ?: {meetingLink}' )
        print('send Registration Verification')

        connection = db.engine.connect()
        try:
            sql = text("""update my_unimo_client_details set token=:token where id=:id""")
            connection.execute(sql, {"token": token, "id": id})
            connection.commit()  # Manually commit the transaction
        except Exception as e:
            print(f"An error occurred: {e}")
            connection.rollback()
        finally:
            connection.close()

        subject = f'a request for {serviceName} Services'

        send = mailSend(email, body, 'Registration', subject, 'Service Request')

        if send:
            return verification_url
        else:
            return False

    except Exception as e:
        print('Email Send Exception', e)

        errorMessage = f'{e}'
        url = '/api/v1/mail/sendInvitation'
        function = 'sendInvitation'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return "Mail send failed"
        else:
            return "Mail send failed. Error Log Save Failed"


# Type is for which service mail want to send from that service subject, title, details will retrieve
def mailSend(emailTo, emailMessage, type, subject, title):
    try:
        print('emailTo', emailTo)
        print('emailMessage', emailMessage)

        getMailSettings = getActiveMailConfiguration(type)
        getMailSettings = mailConfigureWithDto.dump(getMailSettings)
        print(getMailSettings)
        cipher_suite = Fernet(getMailSettings['key'])
        encrypted_password = getMailSettings['password']
        password = cipher_suite.decrypt(encrypted_password.encode()).decode()

        sender = getMailSettings['senderEmail']
        host = getMailSettings['server']
        port = getMailSettings['port']
        if subject == '':
            subject = getMailSettings['subject']
        else:
            subject = subject

        if title == '':
            sender_title = getMailSettings['senderTitle']
        else:
            sender_title = title

        recipient = emailTo
        html = emailMessage

        # Create message
        message = MIMEMultipart()
        message.attach(MIMEText(html, "html"))
        message['Subject'] = Header(subject, 'utf-8')
        message['From'] = formataddr((str(Header(sender_title, 'utf-8')), sender))
        message['To'] = emailTo

        # Create server object with SSL option
        # print('connecting to the server...', host, port, type(host), type(port), sender, password)
        # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server = smtplib.SMTP_SSL(host, port)
        server.login(sender, password)

        server.sendmail(sender, recipient, message.as_string().encode('ascii', 'ignore'))
        server.quit()

        print('Email sent successfully.')

        print('Sent',)
        return True

    except Exception as e:
        print('Email Send Exception', e)

        errorMessage = f'{e}'
        url = '/api/v1/mail/emailSend'
        function = 'mailSend'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return "Mail send failed"
        else:
            return "Mail send failed. Error Log Save Failed"


def invitationVerify(verify):
    try:
        tokenChecker = MyUnimoClientDetails.query.filter_by(token=verify).first()
        print('tokenChecker', tokenChecker)
        if tokenChecker:
            print(tokenChecker.id)
            connection = db.engine.connect()
            try:
                sql = text("""update my_unimo_client_details set request_status='Accepted' where id=:id""")
                connection.execute(sql, {"id": tokenChecker.id})
                connection.commit()  # Manually commit the transaction
            except Exception as e:
                print(f"An error occurred: {e}")
                connection.rollback()
            finally:
                connection.close()

            return True
        else:
            return False

    except Exception as e:
        print("Error Email verification ===>", e)
        return False


def mailVerification(email, token):
    try:
        print(email, token)
        emailChecker = UsersLoginInformation.query.filter_by(email=email).first()
        print('emailChecker', emailChecker)
        if emailChecker:
            print(emailChecker.token, emailChecker.expirationTime, emailChecker.emailVerified)
            if emailChecker.emailVerified:
                return {"type": False, "message": "Your email is verified successfully", "status": "success"}
            else:
                if token == emailChecker.token:
                    if datetime.utcnow() < emailChecker.expirationTime:
                        connection = db.engine.connect()
                        try:
                            # if emailChecker.userType == 'Immigrant':
                            sql = text("""update users_login set is_active=True, email_verified=True
                                            where email=:email""")
                            connection.execute(sql, {"email": email})
                            connection.commit()  # Manually commit the transaction
                            # elif emailChecker.userType == 'Professional':
                            #     sql = text("""update users_login set email_verified=True where email=:email""")
                            #     connection.execute(sql, {"email": email})
                            #     connection.commit()  # Manually commit the transaction
                        except Exception as e:
                            print(f"An error occurred: {e}")
                            connection.rollback()
                        finally:
                            connection.close()
                        return {"type": True, "message": "Your email is verified successfully", "status": "success"}
                    else:
                        return {"type": False, "message": "Session time is expired", "status": "failed"}
                else:
                    return {"type": False, "message": "Invalid token", "status": "failed"}
        else:
            return {"type": False, "message": "This email is not registered", "status": "failed"}

    except Exception as e:
        print("Error Email verification ===>", e)