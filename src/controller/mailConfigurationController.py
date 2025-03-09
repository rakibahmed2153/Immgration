# Libraries Declartion
from flask import Blueprint, request, Response, json

# Import Local Files
from src.model.products.mailConfig.mailConfig import *
from src.model.products.errorLog.errorLog import errorLogSave

# -------- Controller Blueprint Create ----------
mailController = Blueprint('mailController', __name__)


@mailController.route('/saveMailConfig', methods=['POST'])
def saveMailConfig():
    try:
        print(' saveMailConfig: ')
        data = request.get_json()
        # print(' json: ', jsonData)
        # data = data['params']

        saveRecord = mailConfigurationSave(data)
        status = 'success'
        statusCode = 200

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': saveRecord}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('Mail Config Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/mail/saveMailConfig'
        function = 'saveMailConfig'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@mailController.route('/verify', methods=['GET'])
def verifyEmail():
    try:
        email = request.args.get('email', None)
        token = request.args.get('token', None)

        if token == '' or token is None or email == '' or email is None:
            saveRecord = 'Fields are missing'
            status = 'failed'
            statusCode = 201
        else:
            verify = mailVerification(email, token)
            saveRecord = verify['message']
            status = verify['status']
            if verify['status'] == 'failed':
                statusCode = 201
            else:
                statusCode = 200

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': saveRecord}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('Mail Config Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/mail/saveMailConfig'
        function = 'saveMailConfig'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@mailController.route('/confirmationSend', methods=['GET'])
def confirmationSend():
    try:
        email = request.args.get('email', None)

        emailCheck = UsersLoginInformation.query.filter_by(email=email).first()
        print('emailCheck', emailCheck)
        if emailCheck:
            mail = sendRegistrationVerification(email)
            if mail:
                saveRecord = 'Mail Send Successfully'
                status = 'success'
                statusCode = 200
            else:
                saveRecord = 'Mail send failed'
                status = 'failed'
                statusCode = 201
        else:
            saveRecord = 'This email is not registered'
            status = 'failed'
            statusCode = 201

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': saveRecord}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('Mail Config Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/mail/saveMailConfig'
        function = 'saveMailConfig'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')

