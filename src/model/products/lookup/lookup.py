from src.services.sql.queryExecute import dataFetch
from src.model.products.errorLog.errorLog import *


def getLookData(lookupCode, levelCode):
    try:
        and_clause = ["%s = '%s'" % ('lookup_code', lookupCode), "%s = '%s'" % ('level_code', levelCode)]
        tableDetails = "id, level_data from lookup_data"
        and_clause_str = ' AND '.join(and_clause)
        sql_query = 'select ' + tableDetails + ' where ' + and_clause_str + ' order by created_date asc;'
        lookupList = dataFetch(sql_query, 'all')
        return lookupList

    except Exception as e:
        print('Lookup Error ===> ', e)
        # ========= Error Log Creation ==========
        errorMessage = f'{e}'
        url = '/api/v1/look/getLookData'
        function = 'getLookData'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return []
        else:
            return []


def getLookDataWithParent(lookupCode, levelCode, parentId):
    try:
        and_clause = ["%s = '%s'" % ('lookup_code', lookupCode), "%s = '%s'" % ('level_code', levelCode),
                      "%s = '%s'" % ('parent_id', parentId)]
        tableDetails = "id, level_data from lookup_data"
        and_clause_str = ' AND '.join(and_clause)
        sql_query = 'select ' + tableDetails + ' where ' + and_clause_str + ' order by created_date asc;'
        lookupList = dataFetch(sql_query, 'all')
        return lookupList

    except Exception as e:
        print('Lookup Error ===> ', e)
        # ========= Error Log Creation ==========
        errorMessage = f'{e}'
        url = '/api/v1/look/getLookData'
        function = 'getLookData'

        errorSave = errorLogSave(url, function, errorMessage)

        if errorSave == "success":
            return []
        else:
            return []