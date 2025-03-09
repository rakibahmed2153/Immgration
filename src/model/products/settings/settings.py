
from src.model.entity.entity import db

# ======== Import Dto, Entity ===========
from src.services.sql.queryExecute import dataFetch
from src.model.entity.settings.settings import PolicyDetails
from src.model.dto.settings.settings import PolicyDetailsDto, PolicyDetailsDtoList
from src.model.products.errorLog.errorLog import errorLogSave

policyDetailsDto = PolicyDetailsDto()
policyDetailsDtoList = PolicyDetailsDtoList()
policyDetailsDtoListAll = PolicyDetailsDtoList(many=True)


def savePolicyDetails(userId, data):
    try:
        print('savePolicyDetails')

        policy = PolicyDetails(
            policyDetails=data['policyDetails'],
            policyTypeId=data['policyTypeId'],
            createdBy=userId,
            lastUpdatedBy=userId,
        )
        db.session.add(policy)
        db.session.commit()
        result = policyDetailsDto.dump(policy)
        print('res', result)

        return {"statusCode": 200, "message": "Policy Details saved.", "status": "success"}

    except Exception as e:
        print('My Unimo Update Exception ===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/settings/savePolicyDetails'
        function = 'savePolicyDetails'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return {"statusCode": 201, "message": "My Unimo history saved failed.", "status": "failed"}
        else:
            return {"statusCode": 201, "message": "My Unimo history saved failed. Error log failed", "status": "failed"}


def getPolicyDetails(policyTypeId):
    try:
        and_clause = ["%s = '%s'" % ('policy_type_id', policyTypeId)]
        tableDetails = " * from policy_details "
        and_clause_str = ' AND '.join(and_clause)
        sql_query = 'select ' + tableDetails + ' where ' + and_clause_str
        policy = dataFetch(sql_query, 'one')

        policyDetails = policyDetailsDtoList.dump(policy)

        return policyDetails

    except Exception as e:
        print('Policy Details Exception===> ', e)

        errorMessage = f'{e}'
        url = '/api/v1/settings/getPolicyDetails'
        function = 'getPolicyDetails'

        # ========= Error Log Creation ==========
        errorSave = errorLogSave(url, function, errorMessage)

        return ''
