from flask import Blueprint, Response, json, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.model.products.errorLog.errorLog import errorLogSave
from src.model.products.settings.settings import *

# -------- Controller Blueprint Create ----------
settingsController = Blueprint('settingsController', __name__)


# Policy Create
####################################
@settingsController.route('/createPolicyData', methods=['POST'])
@jwt_required()
def createPolicyData():
    try:
        print(' createPolicyData ')
        userId = get_jwt_identity()
        print('userId', userId)

        data = request.get_json()
        print(' json: ', data)
        data = data['options']

        # ====== Create data ======
        details = savePolicyDetails(userId, data)

        message = details['message']
        status = details['status']
        statusCode = details['statusCode']

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': message}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('createPolicyData Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/settings/createPolicyData'
        function = 'createPolicyData'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@settingsController.route('/getPolicyByType', methods=['GET'])
def getPolicyByType():
    try:
        print(' getPolicyByType ')
        policyTypeId = request.args.get('policyTypeId', None)  # if name empty then default value will be none
        print('policyTypeId: ', policyTypeId)
        # ====== get data ======
        details = getPolicyDetails(policyTypeId)

        data = details
        status = 'success'
        statusCode = 200

        # print('signUp')
        return Response(json.dumps({'status': status, 'data': data}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('getProfessionalDetails Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/getProfessionalDetails'
        function = 'getProfessionalDetails'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')
