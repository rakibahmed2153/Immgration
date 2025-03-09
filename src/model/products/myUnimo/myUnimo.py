# ======== Import Libraries ===========
from src.model.entity.entity import db
from sqlalchemy import text
from src.services.sql.queryExecute import dataFetch
# ======== Import Dto, Entity ===========
from src.model.entity.myUnimo.myUnimo import MyUnimoClientDetails, MyUnimoClientDetailsHistory
from src.model.dto.myUnimo.myUnimo import (MyUnimoClientDetailsDto, MyUnimoClientDetailsHistoryDto,
                                           MyUnimoClientDetailsDtoList, MyUnimoClientDetailsHistoryDtoList)
from src.model.entity.login.login import UsersLoginInformation
from src.model.products.errorLog.errorLog import *

myUnimoClientDetailsDto = MyUnimoClientDetailsDto()
myUnimoClientDetailsDtoList = MyUnimoClientDetailsDtoList()
myUnimoClientDetailsDtoListAll = MyUnimoClientDetailsDtoList(many=True)

myUnimoClientDetailsHistoryDto = MyUnimoClientDetailsHistoryDto()
myUnimoClientDetailsHistoryDtoList = MyUnimoClientDetailsHistoryDtoList()
myUnimoClientDetailsHistoryDtoListAll = MyUnimoClientDetailsHistoryDtoList(many=True)

from src.model.dto.uploadDocuments.uploadDocuments import UploadDocumentsDtoList
uploadDocumentsDtoList = UploadDocumentsDtoList()
uploadDocumentsDtoListAll = UploadDocumentsDtoList(many=True)

def myUnimoClientDetailsSave(data, userId):
    try:
        print('myUnimoClientDetailsSave')

        print(data, userId)

        myUnimo = MyUnimoClientDetails(
            serviceName=data['serviceName'],
            serviceId=data['serviceId'],
            serviceStepsId=data['serviceStepsId'],
            clientEmail=data['clientEmail'],
            stepNo=data['stepNo'],
            employeeName=data['employeeName'],
            clientPortalLink=data['clientPortalLink'],
            meetingLink=data['meetingLink'],
            userId=userId,
            currentClient=False,
        )
        db.session.add(myUnimo)
        db.session.commit()
        result = myUnimoClientDetailsDto.dump(myUnimo)
        print('My unimo client details save', result['id'])

        return {"statusCode": 200, "message": "Invitation sent to the client successfully", "status": "success",
                "id": result['id']}

    except Exception as e:
        print('My Service Save Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/service/myServiceSave'
        function = 'myServiceSave'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return {"statusCode": 201, "message": "Invitation sent failed.", "status": "failed", "id": ''}
        else:
            return {"statusCode": 201, "message": "Invitation sent failed. Error log failed", "status": "failed",
                    "id": ''}


def getMyUnimoClientDetails(userId, type):
    try:
        print('userId ---->', userId)

        details = UsersLoginInformation.query.filter_by(id=userId).first()
        print('userId', details.email)

        if type == 'currentClient':
            if details.userType == 'Immigrant':
                and_clause = ["%s = '%s'" % ('client_email', details.email), "%s = %s" % ('current_client', True)]
            else:
                and_clause = ["%s = '%s'" % ('user_id', userId), "%s = %s" % ('current_client', True)]
        else:
            and_clause = ["%s = '%s'" % ('user_id', userId)]

        tableDetails = (" mucd.*, msd.label_details, msd.label_name from my_unimo_client_details mucd "
                        " left join my_service_details msd on msd.id=mucd.service_steps_id ")
        and_clause_str = ' AND '.join(and_clause)
        sql_query = 'select ' + tableDetails + ' where ' + and_clause_str + ' order by created_date asc'
        services = dataFetch(sql_query, 'all')

        servicesList = myUnimoClientDetailsDtoListAll.dump(services)

        return servicesList

    except Exception as e:
        print('Get My client Details Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/myunimo/getMyUnimoClientDetails'
        function = 'getMyUnimoClientDetails'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return {"statusCode": 201, "message": "My service saved failed.", "status": "failed"}
        else:
            return {"statusCode": 201, "message": "My service saved failed. Error log failed",
                    "status": "failed"}


def getMyUnimoUserDetails(userId):
    try:
        print('userId ---->', userId)
        userId = UsersLoginInformation.query.filter_by(id=userId).first()
        print('userId', userId.email)

        and_clause = ["%s = '%s'" % ('client_email', userId.email)]
        tableDetails = (" md.*, pp.email, msd.label_details, msd.label_name from my_unimo_client_details md "
                        " left join users_login pp on pp.id = md.user_id "
                        " left join my_service_details msd on msd.id=md.service_steps_id ")
        and_clause_str = ' AND '.join(and_clause)
        sql_query = 'select ' + tableDetails + ' where ' + and_clause_str + ' order by created_date asc'
        services = dataFetch(sql_query, 'all')

        servicesList = myUnimoClientDetailsDtoListAll.dump(services)

        return servicesList

    except Exception as e:
        print('Get My client Details Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/myunimo/getMyUnimoDetails'
        function = 'getMyUnimoUserDetails'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return {"statusCode": 201, "message": "My service saved failed.", "status": "failed"}
        else:
            return {"statusCode": 201, "message": "My service saved failed. Error log failed",
                    "status": "failed"}


def updateMyunimoDiscoveryDate(id, discoverCallDate, customerStatus):
    try:
        print('Update Myunimo Discovery Date')

        db.session.query(MyUnimoClientDetails).filter_by(id=id).update({
            'discoverCallDate': discoverCallDate,
            'customerStatus': customerStatus,
        })
        db.session.commit()
        return {"statusCode": 200, "message": "My Unimo Discovery Updated Successfully", "status": "success"}

    except Exception as e:
        print('My Unimo Update Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/myUnimo/updateMyunimoDiscoveryDate'
        function = 'updateMyunimoDiscoveryDate'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return {"statusCode": 201, "message": "My Unimo status update failed.", "status": "failed"}
        else:
            return {"statusCode": 201, "message": "My Unimo status update failed. Error log failed", "status": "failed"}


def getServiceDetailsId(serviceId, stepNo):
    try:
        and_clause = ["%s = '%s'" % ('service_id', serviceId), "%s = '%s'" % ('label_no', stepNo)]
        tableDetails = " id from my_service_details"
        and_clause_str = ' AND '.join(and_clause)
        sql_query = 'select ' + tableDetails + ' where ' + and_clause_str
        services = dataFetch(sql_query, 'one')

        servicesList = myUnimoClientDetailsDtoList.dump(services)

        return servicesList['id']

    except Exception as e:
        print('Get My client Details Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/myunimo/getMyUnimoDetails'
        function = 'getMyUnimoUserDetails'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        return ''


def updateMyunimoToCurrent(id, serviceId, requestStatus, customerStatus):
    try:
        print('Update Myunimo Current')

        if customerStatus == 'Accepted':
            currentClient = True
            stepNo = 2
            serviceStepsId = getServiceDetailsId(serviceId, stepNo)
        else:
            currentClient = False
            stepNo = 1
            serviceStepsId = getServiceDetailsId(serviceId, stepNo)

        db.session.query(MyUnimoClientDetails).filter_by(id=id).update({
            'requestStatus': requestStatus,
            'customerStatus': customerStatus,
            'currentClient': currentClient,
            'stepNo': stepNo,
            'serviceStepsId': serviceStepsId
        })
        db.session.commit()
        history = saveCurrentClientHistory(id, serviceId, serviceStepsId, stepNo, currentClient, '', customerStatus, requestStatus)
        return {"statusCode": 200, "message": "My Unimo Discovery Updated Successfully", "status": "success"}

    except Exception as e:
        print('My Unimo Update Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/myUnimo/updateMyunimoToCurrent'
        function = 'updateMyunimoToCurrent'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return {"statusCode": 201, "message": "My Unimo status update failed.", "status": "failed"}
        else:
            return {"statusCode": 201, "message": "My Unimo status update failed. Error log failed", "status": "failed"}


def updateCurrentClientStatus(id, status):
    try:
        print('My Unimo Update')

        db.session.query(MyUnimoClientDetails).filter_by(id=id).update({
            'currentClientStatus': status,
        })
        db.session.commit()
        history = saveCurrentClientHistory(id, '', '', '', '', status, '', '')
        return {"statusCode": 200, "message": "My Unimo Details Updated Successfully", "status": "success"}

    except Exception as e:
        print('My Unimo Update Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/myUnimo/updateMyunimo'
        function = 'updateMyunimo'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return {"statusCode": 201, "message": "My Unimo status update failed.", "status": "failed"}
        else:
            return {"statusCode": 201, "message": "My Unimo status update failed. Error log failed", "status": "failed"}


def saveCurrentClientHistory(id, serviceId, serviceStepsId, stepNo, currentClient, currentClientStatus,
                             customerStatus, requestStatus):
    try:
        print('saveCurrentClientHistory')
        data = MyUnimoClientDetails.query.filter_by(id=id).first()

        myUnimo = MyUnimoClientDetailsHistory(
            serviceName=data.serviceName,
            serviceId=data.serviceId if serviceId == '' else serviceId,
            serviceStepsId=data.serviceStepsId if serviceStepsId == '' else serviceStepsId,
            clientEmail=data.clientEmail,
            stepNo=data.stepNo if stepNo == '' else stepNo,
            employeeName=data.employeeName,
            clientPortalLink=data.clientPortalLink,
            userId=data.userId,
            currentClient=data.currentClient if currentClient == '' else currentClient,
            currentClientStatus=data.currentClientStatus if currentClientStatus == '' else currentClientStatus,
            customerStatus=data.customerStatus if customerStatus == '' else customerStatus,
            requestStatus=data.requestStatus if requestStatus == '' else requestStatus,
        )
        db.session.add(myUnimo)
        db.session.commit()
        result = myUnimoClientDetailsHistoryDto.dump(myUnimo)
        print('res', result)

        return {"statusCode": 200, "message": "My Unimo history saved.", "status": "success"}

    except Exception as e:
        print('My Unimo Update Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/myUnimo/saveCurrentClientHistory'
        function = 'saveCurrentClientHistory'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return {"statusCode": 201, "message": "My Unimo history saved failed.", "status": "failed"}
        else:
            return {"statusCode": 201, "message": "My Unimo history saved failed. Error log failed", "status": "failed"}


def updateMyunimoData(id, status, serviceId, stepNo):
    try:
        print('My Unimo Update')
        if status == 'Accepted':
            stepNo = stepNo + 1
            serviceStepsId = getServiceDetailsId(serviceId, stepNo)
            if serviceStepsId == '':
                db.session.query(MyUnimoClientDetails).filter_by(id=id).update({
                    'currentClientStatus': status,
                    'currentClient': False,
                })
                db.session.commit()
                history = saveCurrentClientHistory(id, serviceId, serviceStepsId, stepNo, '', status, '', '')
                return {"statusCode": 200, "message": "My Unimo Details Updated Successfully", "status": "success"}
        else:
            stepNo = stepNo
            serviceStepsId = getServiceDetailsId(serviceId, stepNo)

        db.session.query(MyUnimoClientDetails).filter_by(id=id).update({
            'currentClientStatus': status,
            'stepNo': stepNo,
            'serviceStepsId': serviceStepsId,
        })
        db.session.commit()
        history = saveCurrentClientHistory(id, serviceId, serviceStepsId, stepNo, '', status, '', '')
        return {"statusCode": 200, "message": "My Unimo Details Updated Successfully", "status": "success"}

    except Exception as e:
        print('My Unimo Update Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/myUnimo/updateMyunimo'
        function = 'updateMyunimo'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return {"statusCode": 201, "message": "My Unimo status update failed.", "status": "failed"}
        else:
            return {"statusCode": 201, "message": "My Unimo status update failed. Error log failed", "status": "failed"}


def getMyUnimoCalDetails(userId):
    try:
        print('userId ---->', userId)
        users = UsersLoginInformation.query.filter_by(id=userId).first()
        print('userId', users.userType)
        services = []
        if users.userType == 'Professional':
            and_clause = ["%s = '%s'" % ('muc.user_id', userId), "%s is not %s" % ('muc.discover_call_date', 'null')]
            tableDetails = (" muc.discover_call_date as start_date, muc.discover_call_date as end_date,"
                            " CONCAT(ip.first_name, ' ', ip.last_name) as title, ip.email, ul.id as client_id"
                            " from my_unimo_client_details muc"
                            " left join users_login ul on muc.client_email = ul.email"
                            " left join immigrant_profile ip on ul.user_id = ip.id")
            and_clause_str = ' AND '.join(and_clause)
            sql_query = 'select ' + tableDetails + ' where ' + and_clause_str
            services = dataFetch(sql_query, 'all')
        elif users.userType == 'Immigrant':
            and_clause = ["%s = '%s'" % ('muc.client_email', users.email), "%s is not %s" % ('muc.discover_call_date', 'null')]
            tableDetails = (" muc.discover_call_date as start_date, muc.discover_call_date as end_date,"
                            " CONCAT(ip.first_name, ' ', ip.last_name) as title, ip.email, muc.user_id as client_id"
                            " from my_unimo_client_details muc"
                            " left join users_login ul on ul.id = muc.user_id"
                            " left join professional_profile ip on ul.user_id = ip.id")
            and_clause_str = ' AND '.join(and_clause)
            sql_query = 'select ' + tableDetails + ' where ' + and_clause_str
            services = dataFetch(sql_query, 'all')

        servicesList = myUnimoClientDetailsDtoListAll.dump(services)

        print('service', servicesList)

        for item in servicesList:
            # Pro pic
            and_clause = ["%s = '%s'" % ('user_id', item['clientId']), "%s = '%s'" % ('document_type', 'profile_picture')]
            tableDetails = " file_url from user_documents "
            and_clause_str = ' AND '.join(and_clause)
            sql_query = 'select ' + tableDetails + ' where ' + and_clause_str
            print('sql_query', sql_query)
            proPic = dataFetch(sql_query, 'one')
            proPic = uploadDocumentsDtoList.dump(proPic)
            print('pro', proPic)

            if 'fileUrl' in proPic:
                item['profilePicture'] = proPic['fileUrl']
            else:
                item['profilePicture'] = ''

            # User Story
            and_clause = ["%s = '%s'" % ('user_id', item['clientId']), "%s = '%s'" % ('document_type', 'your_story')]
            tableDetails = " file_url from user_documents "
            and_clause_str = ' AND '.join(and_clause)
            sql_query = 'select ' + tableDetails + ' where ' + and_clause_str
            storyPic = dataFetch(sql_query, 'one')
            storyPic = uploadDocumentsDtoList.dump(storyPic)
            print('storyPic', storyPic)

            if 'fileUrl' in storyPic:
                item['storyVideo'] = storyPic['fileUrl']
            else:
                item['storyVideo'] = ''

        print('all', servicesList)

        return {"statusCode": 200, "message": "All Data", "status": "success", "data": servicesList}

    except Exception as e:
        print('Get My client Details Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/myunimo/getMyUnimoDetails'
        function = 'getMyUnimoUserDetails'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return {"statusCode": 201, "message": "My service saved failed.", "status": "failed"}
        else:
            return {"statusCode": 201, "message": "My service saved failed. Error log failed",
                    "status": "failed"}