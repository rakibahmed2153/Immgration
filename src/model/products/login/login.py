# ======== Import Libraries ===========
from passlib.hash import sha256_crypt
from sqlalchemy import text
import re
# ======== Import Dto, Entity ===========
from src.model.entity.login.login import ImmigrantProfile, ProfessionalProfile, UsersLoginInformation
from src.model.dto.login.login import (ImmigrantProfileDto, ImmigrantProfileDtoList, ProfessionalProfileDto,
                                       ProfessionalProfileDtoList, UsersLoginDto, UsersLoginDtoList)
from src.model.entity.myUnimo.myUnimo import MyUnimoClientDetails
from src.model.products.errorLog.errorLog import *

immigrantProfileDto = ImmigrantProfileDto()
immigrantProfileDtoList = ImmigrantProfileDtoList()
immigrantProfileDtoListAll = ImmigrantProfileDtoList(many=True)

professionalProfileDto = ProfessionalProfileDto()
professionalProfileDtoList = ProfessionalProfileDtoList()
professionalProfileDtoListAll = ProfessionalProfileDtoList(many=True)

usersLoginDto = UsersLoginDto()
usersLoginDtoList = UsersLoginDtoList()
usersLoginDtoListAll = UsersLoginDtoList(many=True)


def registrationDetailsSave(data):
    # print('save', data)
    if data['userType'] == 'Immigrant':
        # print('immigrant')
        return immigrantRegistration(data)

    elif data['userType'] == 'Professional':
        # print('Professional')
        return professionalRegistration(data)

    else:
        return "Select a proper Registration Type"


def immigrantRegistration(data):
    try:
        print('Immigrant Registration')
        immigrantProfile = ImmigrantProfile(
            firstName=data['firstName'],
            lastName=data['lastName'],
            email=data['email'],
            phone=data['phone'],
            age=data['age'],
            countryResidence=data['countryResidence'],
            desiredDestination=data['desiredDestination'],
            maritalStatus=data['maritalStatus'],
            familyMembers=data['familyMembers'] if 'familyMembers' in data else None,
            referralSource=data['referralSource'] if 'referralSource' in data else None,
            userType=data['userType'],
            selectedAnswers=data['selectedAnswers'],
            selectedQuestions=data['selectedQuestions'],
        )
        db.session.add(immigrantProfile)
        db.session.commit()
        result = immigrantProfileDto.dump(immigrantProfile)

        # MyUnimo Client Details Update
        updateDetails = myUnimoClientDetailsUpdate(data)

        return usersLoginDetailsSave(data, result['id'])

    except Exception as e:
        print('SignUp Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/login/signUp'
        function = 'immigrantRegistration'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return "Registration Saved Failed"
        else:
            return "Registration Saved Failed. Error Log Save Failed"


def myUnimoClientDetailsUpdate(data):
    try:
        print('myUnimoClientDetailsUpdate')

        details = MyUnimoClientDetails.query.filter_by(clientEmail=data['email']).first()
        print('details', details)

        if details:
            db.session.query(MyUnimoClientDetails).filter_by(id=details.id).update({
                'phone': data['phone'],
                'firstName': data['firstName'],
                'lastName': data['lastName']
            })
            db.session.commit()

        return True

    except Exception as e:
        print('My Unimo Client Details Update Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/login/signUp'
        function = 'myUnimoClientDetailsUpdate'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return False
        else:
            return False


def professionalRegistration(data):
    try:
        print('Professional Registration')
        professionalProfile = ProfessionalProfile(
            firstName=data['firstName'],
            lastName=data['lastName'],
            email=data['email'],
            phone=data['phone'],
            companyLegalName=data['companyLegalName'],
            selectedAnswers=data['selectedAnswers'],
            selectedQuestions=data['selectedQuestions'],
            userType=data['userType']
        )
        db.session.add(professionalProfile)
        db.session.commit()
        result = professionalProfileDto.dump(professionalProfile)
        return usersLoginDetailsSave(data, result['id'])

    except Exception as e:
        print('SignUp Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/login/signUp'
        function = 'professionalRegistration'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return "Registration Saved Failed"
        else:
            return "Registration Saved Failed. Error Log Save Failed"


def usersLoginDetailsSave(data, userId):
    print('Users Login DetailsSave Save')
    try:
        # print('Immigrant Registration', data)
        # Password Encrypt
        password = sha256_crypt.encrypt(data['password'])

        if data['userType'] == 'Immigrant':
            isActive = True
        else:
            isActive = False

        # Save User Profile
        usersProfile = UsersLoginInformation(
            email=data['email'],
            password=password,
            userId=userId,
            userType=data['userType'],
            isLocked=False,
            isActive=isActive,
            lastLogin=None,
            attemptTime=None,
            loginStatus=None,
            emailVerified=False
        )
        db.session.add(usersProfile)
        db.session.commit()
        result = usersLoginDto.dump(usersProfile)
        print('res', result['id'])

        return f"{data['userType']} Registration Successful. A verification mail is sent to your account"

    except Exception as e:

        print('SignUp Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/login/signUp'
        function = 'usersLoginDetailsSave'

        if data['userType'] == 'Immigrant':
            connection = db.engine.connect(close_with_result=True)
            sql = text("""delete from immigrant_profile where id=:id""")
            connection.execute(sql, id=data['id'])
            connection.close()
            db.session.commit()
        elif data['userType'] == 'Professional':
            connection = db.engine.connect(close_with_result=True)
            sql = text("""delete from professional_profile where id=:id""")
            connection.execute(sql, id=data['id'])
            connection.close()
            db.session.commit()

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return "Users Registration Saved Failed"
        else:
            return "Users Registration Saved Failed. Error Log Save Failed"


def is_valid_email(email):
    # Define a regular expression for a basic email format
    email_regex = re.compile(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$')
    # print(re.match(email_regex, email))
    # Check if the email matches the regular expression
    return bool(re.match(email_regex, email))


def registrationValidation(data):
    print('Validation Check', data)

    emailCheck = UsersLoginInformation.query.filter_by(email=data['email']).first()
    print('emailCheck', emailCheck)
    if emailCheck:
        return {"type": False, "message": "This email is already registered", "status": "failed"}

    if data is None:
        return {"type": False, "message": "Please fill up all the mandatory fields", "status": "failed"}

    if data['userType'] == 'Immigrant':

        # Add specific validation conditions for immigrant
        if data['age'] is None or data['age'] == '':
            return {"type": False, "message": "Please fill up age field", "status": "failed"}
        elif data['countryResidence'] is None or data['countryResidence'] == '':
            return {"type": False, "message": "Please fill up country residence field", "status": "failed"}
        elif data['maritalStatus'] is None or data['maritalStatus'] == '':
            return {"type": False, "message": "Please fill up marital status field", "status": "failed"}
        elif data['desiredDestination'] is None or data['desiredDestination'] == '':
            return {"type": False, "message": "Please fill up desired destination field", "status": "failed"}

    if data['userType'] == 'Professional':
        # Add specific validation conditions for Professional
        if data['companyLegalName'] is None or data['companyLegalName'] == '':
            return {"type": False, "message": "Please fill up age field", "status": "failed"}

    if data['firstName'] is None or data['firstName'] == '':
        return {"type": False, "message": "Please fill up first name field", "status": "failed"}
    elif data['lastName'] is None or data['lastName'] == '':
        return {"type": False, "message": "Please fill up last name field", "status": "failed"}
    elif data['phone'] is None or data['phone'] == '':
        return {"type": False, "message": "Please fill up phone number field", "status": "failed"}
    elif data['email'] is None or data['email'] == '':
        return {"type": False, "message": "Please fill up email field", "status": "failed"}
    elif data['password'] is None or data['password'] == '':
        return {"type": False, "message": "Please fill up password field", "status": "failed"}
    elif data['confirmPassword'] is None or data['confirmPassword'] == '':
        return {"type": False, "message": "Please fill up confirm password field", "status": "failed"}
    elif data['password'] != data['confirmPassword']:
        return {"type": False, "message": "Password and confirm password doesn't match", "status": "failed"}
    elif not is_valid_email(data['email']):
        return {"type": False, "message": "Please enter a valid email address", "status": "failed"}
    else:
        return {"type": True, "message": "All valid", "status": "success"}


def authenticateUser(data):
    email = data.get('email')
    entered_password = data.get('password')
    print('User Details check')
    user = UsersLoginInformation.query.filter_by(email=email).first()
    print('emailChecker', user)

    if user:
        if user.emailVerified:
            if user.isActive:
                if user and sha256_crypt.verify(entered_password, user.password):
                    return {"type": False, 'user_id': user.id, 'email': user.email, 'user_type': user.userType,
                            "status": "success", "sendLink": False}
                else:
                    return {"type": False, "message": "Invalid credential, wrong email/password given",
                            "status": "failed", "sendLink": False}
            else:
                return {"type": False, "message": "Please wait for admin to active your account",
                        "status": "failed", "sendLink": False}
        else:
            return {"type": False, "message": "This email is not verified", "status": "failed", "sendLink": True}
    else:
        return {"type": False, "message": "Invalid credential, wrong email/password given",
                "status": "failed", "sendLink": False}


def passwordRetrieval(data):
    email = data.get('email')

    user = UsersLoginInformation.query.filter_by(email=email).first()

    if user:
        user_type = user.userType
        # Get security questions based on user_type
        if user_type == 'Immigrant':
            profile = ImmigrantProfile.query.filter_by(email=email).first()
        elif user_type == 'Professional':
            profile = ProfessionalProfile.query.filter_by(email=email).first()
        else:
            return None
        if profile:
            return {'security_questions': profile.selectedQuestions}
        else:
            return None
    else:
        return None


def securityQuestionsAnswersCheck(data):
    email = data.get('email')
    selectedAnswers = data.get('selectedAnswers')

    user = UsersLoginInformation.query.filter_by(email=email).first()

    if user:
        user_type = user.userType
        # Get security questions based on user_type
        if user_type == 'Immigrant':
            profile = ImmigrantProfile.query.filter_by(email=email).first()
        elif user_type == 'Professional':
            profile = ProfessionalProfile.query.filter_by(email=email).first()
        else:
            return None
        if profile:
            # Check if selectedAnswers match the stored answers
            stored_answers_list = profile.selectedAnswers.replace('{', '').replace('}', '').split(',')
            stored_answers_list = [answer.strip() for answer in stored_answers_list]
            if stored_answers_list == selectedAnswers:
                return {'status': 'success', 'message': 'Security Questions Answers matched'}
            else:
                return {'status': 'failed', 'message': 'Security Questions Answers do not match'}
        else:
            return None
    else:
        return None


def changePasswordFunctionality(data):
    email = data.get('email')
    receivedPassword = data.get('new_password')

    user = UsersLoginInformation.query.filter_by(email=email).first()

    if user:
        user_type = user.userType
        if user_type == 'Immigrant':
            profile = ImmigrantProfile.query.filter_by(email=email).first()
        elif user_type == 'Professional':
            profile = ProfessionalProfile.query.filter_by(email=email).first()
        else:
            return None
        if profile:
            if receivedPassword:
                hashed_password = sha256_crypt.encrypt(receivedPassword)
                user.password = hashed_password
                db.session.commit()
                return {'status': 'success', 'message': 'Password has been changed.'}
            else:
                return {'status': 'failed', 'message': 'Server Error, Please try again.'}
        else:
            return None
    else:
        return None
