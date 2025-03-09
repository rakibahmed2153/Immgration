# -------- Important Libraries Import ------------
from flask import Blueprint, request, Response, json
from src.services.auth.CorsService import CorsService

# -------- Model, DTO, Entity Import ---------
from src.model.products.lookup.lookup import *
from src.model.dto.lookup.lookup import *

# ------------- Object creation ----------

# Lookup Data
lookupDataDtoList = LookupDataDtoList(many=True)
lookupDataDto = LookupDataDto()

# -------- Controller Blueprint Create ----------
lookupController = Blueprint('lookupController', __name__)



@lookupController.after_request
def after_request(resp):
    return CorsService.approveOptions(resp)


@lookupController.before_request
def before_request():

    if request.method == 'OPTIONS':
        resp = Response(json.dumps({'status': 'success', 'message': 'success'}),status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = "*"
        resp.headers['Access-Control-Allow-Methods'] = "POST, GET, OPTIONS, PUT, DELETE, PATCH"
        resp.headers['Access-Control-Allow-Headers'] = "accessToken, content-type"
        return resp


@lookupController.route('/getLookupData', methods=['GET'])
def getLookupData():
    try:
        lookupCode = request.args.get('lookupCode', None)
        print('lookupCode..: ', lookupCode)
        levelId = request.args.get('levelId', None)
        print('levelId..: ', levelId)
        # Lookup Model Class Call
        dataList = getLookData(lookupCode, levelId)
        print('dataList...')
        lookupData = lookupDataDtoList.dump(dataList)
        print('lookupData...', lookupData)
        return Response(json.dumps({'status': 200, 'data': lookupData}), status=200,
                        mimetype='application/json')

    except Exception as e:
        print('Error', e)
        return Response(json.dumps({'status': 400, 'message': e, 'data': []}), status=400,
                                mimetype='application/json')


@lookupController.route('/getLookupDataWithParent', methods=['GET'])
def getLookupDataWithParent():
    try:
        lookupCode = request.args.get('lookupCode', None)
        print('lookupCode..: ', lookupCode)
        levelId = request.args.get('levelId', None)
        print('levelId..: ', levelId)
        parentId = request.args.get('parentId', None)
        print('parentId..: ', parentId)
        # Lookup Model Class Call
        dataList = getLookDataWithParent(lookupCode, levelId, parentId)
        print('dataList...')
        lookupData = lookupDataDtoList.dump(dataList)
        print('lookupData...', lookupData)
        return Response(json.dumps({'status': 200, 'data': lookupData}), status=200,
                        mimetype='application/json')

    except Exception as e:
        print('Error', e)
        return Response(json.dumps({'status': 400, 'message': e, 'data': []}), status=400,
                                mimetype='application/json')