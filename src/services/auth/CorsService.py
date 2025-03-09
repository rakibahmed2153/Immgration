

class CorsService(object):

    def approveOptions(resp):
        resp.headers['Access-Control-Allow-Origin'] = "*"
        resp.headers['Access-Control-Allow-Methods'] = "POST, GET, OPTIONS, PUT, DELETE, PATCH"
        resp.headers['Access-Control-Allow-Headers'] = "accessToken, content-type"
        return resp


