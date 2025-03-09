# ======== Import Libraries ===========
from src.services.sql.queryExecute import dataFetch, queryRun
from src.model.entity.entity import db
from sqlalchemy import text
# ======== Import Dto, Entity ===========
from src.model.entity.myService.myService import MyServiceInformation, MyServiceDetailsInformation
from src.model.dto.myService.myService import (MyServiceDto, MyServiceDtoList, MyServiceDetailsDto,
                                               MyServiceDetailsDtoList)
from src.model.products.errorLog.errorLog import *

myServiceDto = MyServiceDto()
myServiceDtoList = MyServiceDtoList()
myServiceDtoAllList = MyServiceDtoList(many=True)

myServiceDetailsDto = MyServiceDetailsDto()
myServiceDetailsDtoList = MyServiceDetailsDtoList()
myServiceDetailsDtoAllList = MyServiceDetailsDtoList(many=True)


def myServiceSave(data, userId):

    try:
        print('myServiceSave')

        myService = MyServiceInformation(
            service=data['service'],
            categoryId=data['categoryId'],
            subCategoryId=data['subCategoryId'],
            version=data['version'],
            userId=userId,
        )
        db.session.add(myService)
        db.session.commit()
        result = myServiceDto.dump(myService)
        print('My Service Save', result['id'])

        for datas in data['myServiceDetails']:
            myServiceDetail = MyServiceDetailsInformation(
                serviceId=result['id'],
                labelName=datas['labelName'],
                labelDetails=datas['labelDetails'],
                labelNo=datas['labelNo']
            )
            db.session.add(myServiceDetail)
            db.session.commit()
            details = myServiceDetailsDto.dump(myServiceDetail)

        return {"statusCode": 200, "message": "My service save successfully", "status": "success"}

    except Exception as e:
        print('My Service Save Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/service/myServiceSave'
        function = 'myServiceSave'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return {"statusCode": 201, "message": "My service saved failed.", "status": "failed"}
        else:
            return {"statusCode": 201, "message": "My service saved failed. Error log failed", "status": "failed"}


def getMyServiceDetails(userId):
    try:
        print('userId ---->', userId)

        and_clause = ["%s = '%s'" % ('user_id', userId)]
        tableDetails = ("ms.*, ld.level_data as category_name, ld1.level_data as sub_category_name from my_service ms"
                        " left join lookup_data ld on ld.id=ms.category_id"
                        " left join lookup_data ld1 on ld1.id=ms.sub_category_id")
        and_clause_str = ' AND '.join(and_clause)
        sql_query = 'select ' + tableDetails + ' where ' + and_clause_str + ' order by created_date asc'
        services = dataFetch(sql_query, 'all')

        servicesList = myServiceDtoAllList.dump(services)
        # print('servicesList', servicesList)

        for service in servicesList:
            and_clause1 = ["%s = '%s'" % ('service_id', service['id'])]
            tableDetails1 = (" * from my_service_details ")
            and_clause_str1 = ' AND '.join(and_clause1)
            sql_query1 = 'select ' + tableDetails1 + ' where ' + and_clause_str1 + ' order by label_no asc'
            servicesDetails = dataFetch(sql_query1, 'all')

            servicesDetailsList = myServiceDetailsDtoAllList.dump(servicesDetails)
            # print('servicesList', servicesDetailsList)

            service['serviceList'] = servicesDetailsList

        return servicesList

    except Exception as e:
        print('Get My Service Details Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/service/getMyService'
        function = 'getMyServiceDetails'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return {"statusCode": 201, "message": "My service saved failed.", "status": "failed"}
        else:
            return {"statusCode": 201, "message": "My service saved failed. Error log failed", "status": "failed"}


def deleteMyService(userId, serviceId):
    try:
        print('serviceId ---->', serviceId)

        # Fetch the service details to delete
        details_to_delete = db.session.query(MyServiceDetailsInformation).filter_by(serviceId=serviceId).all()

        for detail in details_to_delete:
            # Delete each detail object from the session
            db.session.delete(detail)

        # Fetch the service information to delete
        service_to_delete = db.session.query(MyServiceInformation).filter_by(id=serviceId).first()

        if service_to_delete:
            # Delete the service object from the session
            db.session.delete(service_to_delete)

            # Commit the changes
            db.session.commit()

            print("Items deleted successfully")

            return {"statusCode": 200, "message": "My service delete successful.", "status": "success"}
        else:
            print('Service Record not found')
            return {"statusCode": 404, "message": "Service record not found.", "status": "failed"}

    except Exception as e:
        # Handle exceptions (print or log the error)
        print(f"Error: {e}")
        db.session.rollback()  # Rollback the transaction in case of an error
        print('deleteMyService Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/service/deleteMyService'
        function = 'deleteMyService'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return {"statusCode": 201, "message": "My service saved failed.", "status": "failed"}
        else:
            return {"statusCode": 201, "message": "My service saved failed. Error log failed", "status": "failed"}


def myServiceUpdate(data):

    try:
        print('My Service Update')

        db.session.query(MyServiceInformation).filter_by(id=data['serviceId']).update({
            'service': data['service'],
            'categoryId': data['categoryId'],
            'subCategoryId': data['subCategoryId'],
            'version': data['version'],
        })
        db.session.commit()

        for details in data['myServiceDetails']:
            if 'save' in details:
                myServiceDetail = MyServiceDetailsInformation(
                    serviceId=data['serviceId'],
                    labelName=details['labelName'],
                    labelDetails=details['labelDetails'],
                    labelNo=details['labelNo']
                )
                db.session.add(myServiceDetail)
                db.session.commit()
                details = myServiceDetailsDto.dump(myServiceDetail)

            else:
                db.session.query(MyServiceDetailsInformation).filter_by(id=details['id']).update({
                    'labelName': details['labelName'],
                    'labelDetails': details['labelDetails'],
                })
                db.session.commit()

        return {"statusCode": 200, "message": "My service update successfully", "status": "success"}

    except Exception as e:
        print('My Service Update Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/service/myServiceUpdate'
        function = 'myServiceSaveUpdate'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return {"statusCode": 201, "message": "My service update failed.", "status": "failed"}
        else:
            return {"statusCode": 201, "message": "My service update failed. Error log failed", "status": "failed"}