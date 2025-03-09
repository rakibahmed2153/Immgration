# Libraries Declartion
import base64
from flask import Blueprint, Response, json, current_app as app
from flask_jwt_extended import jwt_required, get_jwt_identity
# Import Local Files
from src.model.products.professional.professional import *
from src.model.dto.login.login import (ProfessionalProfileDtoList, OrganizationProfileDtoList,
                                       ImmigrantProfileDto, ImmigrantProfileDtoList)
from src.model.products.errorLog.errorLog import *
from src.model.products.utility.commonFuntion import *
from src.model.products.immigrant.immigrant import *
professionalProfileDtoList = ProfessionalProfileDtoList()
professionalProfileDtoListAll = ProfessionalProfileDtoList(many=True)
organizationProfileDtoList = OrganizationProfileDtoList()

immigrantProfileDto = ImmigrantProfileDto()
immigrantProfileDtoList = ImmigrantProfileDtoList()
immigrantProfileDtoListAll = ImmigrantProfileDtoList(many=True)

# -------- Controller Blueprint Create ----------
userController = Blueprint('userController', __name__)


# Professional Details Starts
####################################
@userController.route('/updateProfessionalData', methods=['POST'])
@jwt_required()
def updateProfessionalData():
    try:
        print(' updateProfessionalData ')
        userId = get_jwt_identity()
        print('userId', userId)

        data = request.get_json()
        print(' json: ', data)
        data = data['options']

        # ====== update data ======
        details = professionDetailsUpdate(data, userId)

        message = details['message']
        status = details['status']
        statusCode = details['statusCode']

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': message}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('updateProfessionalData Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/updateProfessionalData'
        function = 'updateProfessionalData'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@userController.route('/updateProfessionalPermission', methods=['POST'])
@jwt_required()
def updateProfessionalPermission():
    try:
        print(' updateProfessionalPermission ')
        userId = get_jwt_identity()
        print('userId', userId)

        data = request.get_json()
        print(' json: ', data)
        data = data['options']

        # ====== update data ======
        details = professionPermissionUpdate(data, userId)

        message = details['message']
        status = details['status']
        statusCode = details['statusCode']

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': message}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('updateProfessionalPermission Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/updateProfessionalPermission'
        function = 'updateProfessionalPermission'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@userController.route('/getProfessionalDetails', methods=['GET'])
@jwt_required()
def getProfessionalDetails():
    try:
        print(' getProfessionalDetails ')

        userId = get_jwt_identity()
        print('userId', userId)

        if userId is None or userId == '':
            data = 'Access token is not valid'
            status = 'failed'
            statusCode = 201

        else:
            # ====== get data ======
            details = professionDetails(userId)

            professionalDetails = professionalProfileDtoList.dump(details)
            print('professionalDetails', professionalDetails)

            data = professionalDetails
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


@userController.route('/getEmployeeDetails', methods=['GET'])
@jwt_required()
def getEmployeeDetails():
    try:
        print(' getEmployeeDetails ')

        userId = get_jwt_identity()
        print('userId', userId)

        if userId is None or userId == '':
            data = 'Access token is not valid'
            status = 'failed'
            statusCode = 201

        else:
            # ====== get data ======
            details = employeeDetails(userId)

            professionalDetails = professionalProfileDtoListAll.dump(details)
            print('professionalDetails', professionalDetails)

            data = professionalDetails
            status = 'success'
            statusCode = 200

        # print('signUp')
        return Response(json.dumps({'status': status, 'data': data}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('getEmployeeDetails Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/getEmployeeDetails'
        function = 'getEmployeeDetails'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@userController.route('/allowView', methods=['POST'])
@jwt_required()
def allowView():
    try:
        print(' allowView ')
        userId = get_jwt_identity()
        print('userId', userId)

        user = UsersLoginInformation.query.filter_by(id=userId).first()
        print('UserFind', user.userType)

        if user.userId is None or user.userId == '':
            message = 'Access token is invalid'
            status = 'failed'
            statusCode = 201

        else:
            data = request.get_json()
            print(' json: ', data)
            data = data['options']
            details = {}
            if user.userType == 'Immigrant':
                # ====== update Immigrant data ======
                details = allowImmigrantViewUpdate(data, userId)
            elif user.userType == 'Professional':
                # ====== update Professional data ======
                details = allowViewUpdate(data, userId)

            message = details['message']
            status = details['status']
            statusCode = details['statusCode']

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': message}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('allowView Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/allowView'
        function = 'allowView'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')
# Professional Details Ends
####################################
        

@userController.route('/uploadDocuments', methods=['POST'])
@jwt_required()
def uploadSaveDocuments():
    try:
        user_id = get_jwt_identity()

        if 'file' not in request.files:
            return Response(json.dumps({'status': 'error', 'message': 'No file part'}),
                            status=400, mimetype='application/json')

        files = request.files.getlist('file')
        document_type = request.form.get('document_type', '').lower()
        document_sub_type = request.form.get('document_sub_type', '').lower()

        details = save_document_and_get_url(user_id, files[0], document_type, document_sub_type)

        message = details['message']
        status = details['status']
        statusCode = details['statusCode']

        return Response(json.dumps({'status': status, 'message': message}),
                        status=statusCode, mimetype='application/json')

# def uploadSaveDocuments():
#     try:
#         print('upload_documents')
#         user_id = get_jwt_identity()
#         print('user_id', user_id)

#         # Check if the request has files
#         if 'file' not in request.files:
#             return Response(json.dumps({'status': 'error', 'message': 'No file part'}),
#                             status=400, mimetype='application/json')

#         files = request.files.getlist('file')

#         # Log the received files
#         # print('Received files:', files)

#         # Assuming 'document_type' is part of the request form data
#         document_type = request.form.get('document_type', '').lower()

#         print("Document Type", document_type)

#         if document_type == 'your story':
#             # Handle story document type using save_story_and_get_url
#             details = save_story_and_get_url(user_id, files[0])

#             message = details['message']
#             status = details['status']
#             statusCode = details['statusCode']
#             print("Details of Story", details)
#             return Response(json.dumps({'status': status, 'message': message}),
#                             status=statusCode, mimetype='application/json')

#         # ====== upload documents ======
#         details = uploadDocuments(files, user_id)

#         message = details['message']
#         status = details['status']
#         statusCode = details['statusCode']

#         return Response(json.dumps({'status': status, 'message': message}),
#                         status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('uploadDocuments Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/uploadDocuments'
        function = 'uploadDocuments'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@userController.route('/getUploadFiles', methods=['GET'])
@jwt_required()
def getUploadFiles():
    try:
        print(' getUploadFiles ')

        userId = get_jwt_identity()
        # print('userId', userId)

        if userId is None or userId == '':
            data = 'Access token is not valid'
            status = 'failed'
            statusCode = 201

        else:
            details = uploadDocumentsDetails(userId)
            # print("Details before getUploadFiles", details)
            
            data = [
                {
                    'id': detail.id,
                    'userId': detail.userId,
                    'documentName': detail.documentName if detail.documentName else None,
                    'documentType': detail.documentType if detail.documentType else None,
                    'documentSubType': detail.documentSubType if detail.documentSubType else None,
                    'contentType': detail.contentType if detail.contentType else None,
                    'fileUrl': detail.fileUrl if detail.fileUrl else None,
                    'uploadDate': detail.uploadDate,
                }
                for detail in details
            ]

            # print('getUploadFiles', data)

            message = 'Data fetched successfully'
            status = 'success'
            statusCode = '200'

        return Response(json.dumps({'status': status, 'message': message, 'data': data}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('getUploadFiles Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/getUploadFiles'
        function = 'getUploadFiles'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')
        

@userController.route('/deleteFile', methods=['DELETE'])
@jwt_required()
def deleteClickedFile():
    try:
        print('delete File')

        userId = get_jwt_identity()
        print('userId', userId)

        if userId is None or userId == '':
            data = 'Access token is not valid'
            status = 'failed'
            statusCode = 201
            return Response(json.dumps({'status': status, 'message': data}), status=statusCode,
                            mimetype='application/json')

        else:
            idForDelete = request.args.get('id', None)  # if name empty then default value will be none
            print('id: ', idForDelete)

            if idForDelete is None:
                return Response(json.dumps({'status': 'failed', 'message': 'No data provided to delete.'}), status=200,
                                mimetype='application/json')

            delete = deleteFile(idForDelete)

            data = delete['message']
            status = delete['status']
            statusCode = delete['statusCode']

            return Response(json.dumps({'status': status, 'message': data}), status=statusCode,
                            mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('delete File Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/deleteFile'
        function = 'deleteFile'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')
        

@userController.route('/<path:filename>')
def download_file(filename):
    file_path = os.path.join(app.config['fileUploadPath'], filename)
    return send_file(file_path)


# Organization Details Starts
####################################
@userController.route('/saveOrganizationDetails', methods=['POST'])
@jwt_required()
def saveOrganizationDetails():
    try:
        print(' saveOrganizationDetails ')
        userId = get_jwt_identity()
        print('userId', userId)

        data = request.get_json()
        print(' json: ', data)
        data = data['options']

        # ====== update data ======
        details = organizationProfileDetails(data, userId)

        message = details['message']
        status = details['status']
        statusCode = details['statusCode']

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': message}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('updateProfessionalData Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/updateProfessionalData'
        function = 'updateProfessionalData'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@userController.route('/getOrganizationDetails', methods=['GET'])
@jwt_required()
def getOrganizationDetails():
    try:
        print(' getOrganizationDetails ')

        userId = get_jwt_identity()
        # print('userId', userId)

        if userId is None or userId == '':
            data = 'Access token is not valid'
            status = 'failed'
            statusCode = 201

        else:
            details = organizationDetails(userId)
            orgDetails = organizationProfileDtoList.dump(details)
            print(orgDetails)
            data = orgDetails
            status = 'success'
            statusCode = 200

        return Response(json.dumps({'status': status, 'data': data}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('Get Organization Details Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/getOrganizationDetails'
        function = 'getOrganizationDetails'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@userController.route('/allowOrgView', methods=['POST'])
@jwt_required()
def allowOrgView():

    try:
        print(' allowOrgView ')
        userId = get_jwt_identity()
        print('userId', userId)

        data = request.get_json()
        print(' json: ', data)
        data = data['options']

        # ====== update data ======
        details = allowOrgViewUpdate(data, userId)

        message = details['message']
        status = details['status']
        statusCode = details['statusCode']

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': message}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('allowView Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/allowView'
        function = 'allowView'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')
# Organization Details End
####################################


# Immigrant Details Starts
####################################
@userController.route('/getImmigrantDetails', methods=['GET'])
@jwt_required()
def getImmigrantDetails():
    try:
        print(' getImmigrantDetails ')

        userId = get_jwt_identity()
        print('userId', userId)

        if userId is None or userId == '':
            data = 'Access token is not valid'
            status = 'failed'
            statusCode = 201

        else:
            # ====== get data ======
            details = immigrantDetails(userId)
            print(details)
            ImmigrantDetails = immigrantProfileDtoList.dump(details)
            print('ImmigrantDetails', ImmigrantDetails)

            data = ImmigrantDetails
            status = 'success'
            statusCode = 200

        # print('signUp')
        return Response(json.dumps({'status': status, 'data': data}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('getImmigrantDetails Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/getImmigrantDetails'
        function = 'getImmigrantDetails'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@userController.route('/updateImmigrantData', methods=['POST'])
@jwt_required()
def updateImmigrantData():
    try:
        print(' updateImmigrantData ')
        userId = get_jwt_identity()
        print('userId', userId)

        data = request.get_json()
        print(' json: ', data)
        data = data['options']

        # ====== update data ======
        details = immigrantDetailsUpdate(data, userId)

        message = details['message']
        status = details['status']
        statusCode = details['statusCode']

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': message}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('updateImmigrantData Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/updateImmigrantData'
        function = 'updateImmigrantData'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@userController.route('/allowImmigrantView', methods=['POST'])
@jwt_required()
def allowImmigrantView():
    try:
        print(' allowImmigrantView ')
        userId = get_jwt_identity()
        print('userId', userId)

        data = request.get_json()
        print(' json: ', data)
        data = data['options']

        # ====== update data ======
        details = allowImmigrantViewUpdate(data, userId)

        message = details['message']
        status = details['status']
        statusCode = details['statusCode']

        # print('signUp')
        return Response(json.dumps({'status': status, 'message': message}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('allowView Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/allowView'
        function = 'allowView'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')


@userController.route('/getUserDetails', methods=['GET'])
@jwt_required()
def getUserDetails():
    try:
        print(' getUserDetails ')

        userId = get_jwt_identity()
        print('userId', userId)

        user = UsersLoginInformation.query.filter_by(id=userId).first()
        print('UserFind', user.userType)

        if user.userId is None or user.userId == '':
            data = 'Access token is not valid'
            status = 'failed'
            statusCode = 201

        else:
            # ====== get data ======
            if user.userType == 'Immigrant':
                details = immigrantDetails(userId)
                print(details)
                ImmigrantDetails = immigrantProfileDtoList.dump(details)
                print('ImmigrantDetails', ImmigrantDetails)

                data = ImmigrantDetails
                status = 'success'
                statusCode = 200

            elif user.userType == 'Professional':
                details = professionDetails(userId)
                professionalDetails = professionalProfileDtoList.dump(details)
                print('professionalDetails', professionalDetails)

                data = professionalDetails
                status = 'success'
                statusCode = 200
            else:
                data = 'Invalid User Type'
                status = 'failed'
                statusCode = 201
        # print('signUp')
        return Response(json.dumps({'status': status, 'data': data}),
                        status=statusCode, mimetype='application/json')

    except Exception as e:
        # ========= Error Log Creation ==========
        print('getUserDetails Exception ===> ', e)
        errorMessage = f'{e}'
        url = '/api/v1/user/getUserDetails'
        function = 'getUserDetails'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error"}),
                            status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'failed', 'message': "Internal Server Error. Error log failed"}),
                            status=201, mimetype='application/json')