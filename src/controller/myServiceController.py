# Libraries Declartion
from flask import Blueprint, request, Response, json
from flask_jwt_extended import jwt_required, get_jwt_identity
# Import Local Files
from src.model.products.myService.myService import *

# -------- Controller Blueprint Create ----------
myServiceController = Blueprint('myServiceController', __name__)


@myServiceController.route('/saveMyService', methods=['POST'])
@jwt_required()
def saveMyService():
    try:
        print(' saveMyService ')
        userId = get_jwt_identity()
        print('userId', userId)
        data = request.get_json()
        print(' json: ', data)
        data = data['options']
        print(' json: ', data)

        # ====== Save Service data ======
        details = myServiceSave(data, userId)

        message = details['message']
        status = details['status']
        statusCode = details['statusCode']

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': message}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('saveMyService Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/service/saveMyService'
        function = 'saveMyService'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@myServiceController.route('/getMyService', methods=['GET'])
@jwt_required()
def getMyService():
    try:
        print(' getMyService ')

        userId = get_jwt_identity()
        print('userId', userId)

        if userId is None or userId == '':
            data = 'Access token is not valid'
            status = 'failed'
            statusCode = 201

        else:
            # ====== get data ======
            details = getMyServiceDetails(userId)

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


@myServiceController.route('/deleteService', methods=['DELETE'])
@jwt_required()
def deleteService():
    try:
        print('delete Service')

        userId = get_jwt_identity()
        print('userId', userId)

        if userId is None or userId == '':
            data = 'Access token is not valid'
            status = 'failed'
            statusCode = 201
            return Response(json.dumps({'status': status, 'message': data}), status=statusCode,
                            mimetype='application/json')

        else:

            idForDelete = request.args.get('serviceId', None)  # if name empty then default value will be none
            print('id: ', idForDelete)

            if idForDelete is None:
                return Response(json.dumps({'status': 'failed', 'message': 'No data provided to delete.'}), status=200,
                                mimetype='application/json')

            delete = deleteMyService(userId, idForDelete)

            print('delete', delete)

            data = delete['message']
            status = delete['status']
            statusCode = delete['statusCode']

            return Response(json.dumps({'status': status, 'message': data}), status=statusCode,
                            mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('deleteService Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/service/deleteService'
        function = 'deleteService'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@myServiceController.route('/updateMyService', methods=['POST'])
def updateMyService():
    try:
        print(' updateMyService ')
        data = request.get_json()
        # print(' json: ', data)
        data = data['options']
        print(' json: ', data)

        # ====== Save Service data ======
        details = myServiceUpdate(data)

        message = details['message']
        status = details['status']
        statusCode = details['statusCode']

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': message}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('saveMyService Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/service/saveMyService'
        function = 'saveMyService'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')
