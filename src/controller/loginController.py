# Libraries Declartion
from flask import Blueprint, request, Response, json
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

# Import Local Files
from src.model.products.login.login import *
from src.model.products.errorLog.errorLog import *


# -------- Controller Blueprint Create ----------
loginController = Blueprint('loginController', __name__)


@loginController.route('/signUp', methods=['POST'])
def signUp():
    try:
        print(' Sign: ')
        data = request.get_json()
        # print(' json: ', jsonData)
        data = data['options']

        # ====== Validation Check ======
        validationCheck = registrationValidation(data)
        print('validationCheck', validationCheck)

        # print(' json: ', jsonData)
        if validationCheck['type']:
            saveRecord = registrationDetailsSave(data)
            status = 'success'
            statusCode = 200
        else:
            saveRecord = validationCheck['message']
            status = validationCheck['status']
            statusCode = 202

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': saveRecord}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('SignUp Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/login/signUp'
        function = 'signUp'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@loginController.route('/signIn', methods=['POST'])
def signIn():
    try:
        print('sign In')
        data = request.get_json()
        data = data['options']
        
        # Authentication Check
        user_data = authenticateUser(data)

        # Set a longer expiration time (e.g., 7 days)
        expires_delta = timedelta(days=7)

        if 'user_id' in user_data:
            # If authentication is successful, create an access token
            access_token = create_access_token(identity=user_data['user_id'], expires_delta=expires_delta)
            return Response(json.dumps({'status': 'success', 'user_id': user_data['user_id'],
                                        'user_type': user_data['user_type'], 'access_token': access_token,
                                        'message': "Logged in successfully"}), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({'status': user_data['status'], 'message': user_data['message'],
                                        'sendLink': user_data['sendLink']}), status=201, mimetype='application/json')
        
    except Exception as e:
        print('Error', e)


@loginController.route('/forgotPassword', methods=['POST'])
def forgotPassword():
    try:
        print('forgot password')
        data = request.get_json()
        data = data['options']
        
         # Authentication Check
        user_data = passwordRetrieval(data)

        if user_data:
            # If authentication is successful, create an access token
            security_questions = user_data['security_questions']
            return Response(json.dumps({'status': 'success', 'security_questions': security_questions,
                                        'message':"Please answer the security questions!!"}),
                            status=200, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Invalid Request/User not found"}),
                            status=201, mimetype='application/json')
        
    except Exception as e:
        print('Error', e)


@loginController.route('/securityQuestionsCheck', methods=['POST'])
def securityQuestionsCheck():
    try:
        print('securityQuestionsCheck')
        data = request.get_json()
        data = data['options']
        
        # Security Questions Check with Stored Answers
        result = securityQuestionsAnswersCheck(data)

        if result['status'] == 'success':
            return Response(json.dumps(result),
                            status=200, mimetype='application/json')
        else:
            return Response(json.dumps(result),
                            status=201, mimetype='application/json')
        
    except Exception as e:
        print('Error', e)


@loginController.route('/changePassword', methods=['POST'])
def changePassword():
    try:
        print('changePassword')
        data = request.get_json()
        data = data['options']
        
        # Change Password Functionality
        result = changePasswordFunctionality(data)

        if result['status'] == 'success':
            return Response(json.dumps(result),
                            status=200, mimetype='application/json')
        else:
            return Response(json.dumps(result),
                            status=201, mimetype='application/json')
        
    except Exception as e:
        print('Error', e)


@loginController.route('/validateAccessToken', methods=['GET'])
@jwt_required()
def validateAccessToken():
    try:
        # The access token is valid if it reaches here
        current_user = get_jwt_identity()
        return Response(json.dumps({'status': 'success'}),
                                status=200, mimetype='application/json')
    except Exception as e:
        print('Error validating access token:', e)
        return Response(json.dumps({'status': 'error', 'message':'Invalid User Credentials'}),
                                status=401, mimetype='application/json')


