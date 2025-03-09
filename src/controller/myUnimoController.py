# Libraries Declartion
from flask import Blueprint, request, Response, json
from flask_jwt_extended import jwt_required, get_jwt_identity
# Import Local Files
from src.model.products.myUnimo.myUnimo import *
from src.model.products.errorLog.errorLog import errorLogSave
from src.model.products.mailConfig.mailConfig import sendInvitation, invitationVerify, mailSend

# -------- Controller Blueprint Create ----------
myUnimoController = Blueprint('myUnimoController', __name__)


@myUnimoController.route('/saveClientInvitation', methods=['POST'])
@jwt_required()
def saveClientInvitation():
    try:
        print(' saveClientInvitation ')
        userId = get_jwt_identity()
        print('userId', userId)
        data = request.get_json()
        print(' json: ', data)
        data = data['options']
        print(' json: ', data)

        # ====== Save My Unimo Client Invitation Details data ======
        details = myUnimoClientDetailsSave(data, userId)

        message = details['message']
        status = details['status']
        statusCode = details['statusCode']
        id = details['id']

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': message, 'id': id}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('saveClientInvitation Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/myunimo/saveClientInvitation'
        function = 'saveClientInvitation'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@myUnimoController.route('/getMyUnimoDetails', methods=['GET'])
@jwt_required()
def getMyUnimoDetails():
    try:
        print(' getMyUnimoDetails ')

        userId = get_jwt_identity()
        print('userId', userId)

        if userId is None or userId == '':
            data = 'Access token is not valid'
            status = 'failed'
            statusCode = 201

        else:
            # ====== get data ======
            details = getMyUnimoUserDetails(userId)

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


@myUnimoController.route('/getMyUnimoClient', methods=['GET'])
@jwt_required()
def getMyUnimoClient():
    try:
        print(' getMyService ')

        userId = get_jwt_identity()
        print('userId', userId)

        type = request.args.get('type', None)
        print('type', type)

        if userId is None or userId == '':
            data = 'Access token is not valid'
            status = 'failed'
            statusCode = 201

        else:
            # ====== get data ======
            details = getMyUnimoClientDetails(userId, type)

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


@myUnimoController.route('/invitationSend', methods=['GET'])
# @jwt_required()
def invitationSend():
    try:
        # userId = get_jwt_identity()
        # print('userId', userId)

        email = request.args.get('email', None)
        id = request.args.get('id', None)
        serviceName = request.args.get('serviceName', None)
        meetingLink = request.args.get('meetingLink', None)

        mail = sendInvitation(email, id, serviceName, meetingLink)

        if mail != '':
            saveRecord = 'Invitation Mail Send Successfully'
            status = 'success'
            link = mail
            statusCode = 200
        else:
            saveRecord = 'Invitation Mail send failed'
            status = 'failed'
            link = ''
            statusCode = 201

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': saveRecord, 'data': link}),
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


@myUnimoController.route('/verifyInvitation', methods=['GET'])
# @jwt_required()
def verifyInvitation():
    try:
        # userId = get_jwt_identity()
        # print('userId', userId)

        verify = request.args.get('verify', None)
        print('token', verify)

        if verify is not None:
            print('got')
            mail = invitationVerify(verify)

            if mail:
                saveRecord = 'Verify Invitation and Request Accepted'
                status = 'success'
                statusCode = 200
            else:
                saveRecord = 'Wrong token given'
                status = 'failed'
                statusCode = 201
        else:
            print('not')
            saveRecord = 'No Token Provided'
            status = 'failed'
            statusCode = 201

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': saveRecord}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('Verify Invitation Config Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/mail/verifyInvitation'
        function = 'verifyInvitation'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@myUnimoController.route('/updateDiscoveryDate', methods=['GET'])
@jwt_required()
def updateDiscoveryDate():
    try:
        print(' updateDiscoveryDate ')

        userId = get_jwt_identity()
        print('userId', userId)

        discoveryDate = request.args.get('discoveryDate', None)
        customerStatus = request.args.get('customerStatus', None)
        id = request.args.get('id', None)

        print('discoveryDate', discoveryDate, id)

        if userId is None or userId == '':
            data = 'Access token is not valid'
            status = 'failed'
            statusCode = 201

        else:
             # ====== get data ======
             details = updateMyunimoDiscoveryDate(id, discoveryDate, customerStatus)

             data = details['message']
             status = details['status']
             statusCode = details['statusCode']

             body = 'Client sent and discovery date for the service request.'
             subject = 'Service request status changes'
             title = 'My Unimo details'

             myUnimoDetails = MyUnimoClientDetails.query.filter_by(id=id).first()
             userDetails = UsersLoginInformation.query.filter_by(id=myUnimoDetails.userId).first()
             print('userId', userDetails.email)

             send = mailSend(userDetails.email, body, 'Registration', subject, title)
             print('send', send)

        return Response(json.dumps({'status': status, 'message': data}), status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('updateDiscoveryDate Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/myunimo/updateDiscoveryDate'
        function = 'updateDiscoveryDate'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@myUnimoController.route('/updateCurrentStateData', methods=['GET'])
@jwt_required()
def updateCurrentStateData():
    try:
        print(' updateCurrentStateData ')

        userId = get_jwt_identity()
        print('userId', userId)

        requestStatus = request.args.get('requestStatus', None)
        customerStatus = request.args.get('customerStatus', None)
        serviceId = request.args.get('serviceId', None)
        id = request.args.get('id', None)

        print('discoveryDate', requestStatus, id, customerStatus)

        if userId is None or userId == '':
            data = 'Access token is not valid'
            status = 'failed'
            statusCode = 201

        else:
             details = updateMyunimoToCurrent(id, serviceId, requestStatus, customerStatus)

             data = details.message
             status = details.status
             statusCode = details.statusCode

             body = f'Client {customerStatus} the service request.'
             subject = 'Service request status changes'
             title = 'My Unimo details'

             myUnimoDetails = MyUnimoClientDetails.query.filter_by(id=id).first()
             userDetails = UsersLoginInformation.query.filter_by(id=myUnimoDetails.userId).first()
             print('userId', userDetails.email)

             send = mailSend(userDetails.email, body, 'Registration', subject, title)
             print('send', send)

        return Response(json.dumps({'status': status, 'message': data}), status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('updateDiscoveryDate Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/myunimo/updateDiscoveryDate'
        function = 'updateDiscoveryDate'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@myUnimoController.route('/updateCurrentState', methods=['POST'])
@jwt_required()
def updateCurrentState():
    try:
        print(' updateCurrentState ')

        userId = get_jwt_identity()
        print('userId', userId)

        data = request.get_json()
        print(' json: ', data)
        data = data['options']

        currentClientStatus = data['currentClientStatus']
        id = data['id']

        print('discoveryDate', currentClientStatus, id)

        if userId is None or userId == '':
            data = 'Access token is not valid'
            status = 'failed'
            statusCode = 201

        else:
             details = updateCurrentClientStatus(id, currentClientStatus)
             print('details', details)
             data = details['message']
             status = details['status']
             statusCode = details['statusCode']

             body = f'Client {currentClientStatus} the service request.'
             subject = 'Service request status changes'
             title = 'My Unimo details'

             myUnimoDetails = MyUnimoClientDetails.query.filter_by(id=id).first()
             userDetails = UsersLoginInformation.query.filter_by(id=myUnimoDetails.userId).first()
             print('userId', userDetails.email)

             send = mailSend(userDetails.email, body, 'Registration', subject, title)
             print('send', send)

        return Response(json.dumps({'status': status, 'message': data}), status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('updateDiscoveryDate Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/myunimo/updateDiscoveryDate'
        function = 'updateDiscoveryDate'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@myUnimoController.route('/updateMyUnimo', methods=['POST'])
@jwt_required()
def updateMyunimo():
    try:
        print(' updateMyunimo ')
        userId = get_jwt_identity()
        # print('userId', userId)
        data = request.get_json()
        data = data['options']

        currentClientStatus = data['currentClientStatus']
        stepNo = data['stepNo']
        serviceId = data['serviceId']
        id = data['id']

        # ====== Update My Unimo Client Details data ======
        details = updateMyunimoData(id, currentClientStatus, serviceId, stepNo)

        message = details['message']
        status = details['status']
        statusCode = details['statusCode']

        body = f'Profession {currentClientStatus} the steps for more details please login to your portal.'
        subject = 'Service request status changes'
        title = 'My Unimo details'

        myUnimoDetails = MyUnimoClientDetails.query.filter_by(id=id).first()

        send = mailSend(myUnimoDetails.clientEmail, body, 'Registration', subject, title)
        print('send', send)

        return Response(json.dumps({'status': status, 'message': message}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('updateMyunimo Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/myunimo/updateMyunimo'
        function = 'updateMyunimo'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@myUnimoController.route('/myUnimoCalendarDetails', methods=['GET'])
@jwt_required()
def myUnimoCalendarDetails():
    try:
        userId = get_jwt_identity()

        if userId is None or userId == '':
            data = []
            message = 'Access token is not valid'
            status = 'failed'
            statusCode = 201
        else:
            details = getMyUnimoCalDetails(userId)
            data = details['data']
            message = details['message']
            status = details['status']
            statusCode = 200
        # print('signUp')
        return Response(json.dumps({'status': status, 'message': message, 'data': data}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('My Unimo Calendar Details Config Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/mail/myUnimoCalendarDetails'
        function = 'myUnimoCalendarDetails'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')
