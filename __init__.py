print('Backend Application is starting')

# Import Necessary Libraries
import os
from flask import Flask
from flask_cors import cross_origin
from src.services.jsonRead.JsonReadService import JsonReadService
from src.model.entity.entity import db
from src.model.dto.dto import ma
import sys
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv


# Import Login Controller
from src.controller.loginController import loginController
from src.controller.lookupController import lookupController
from src.controller.mailConfigurationController import mailController
from src.controller.userController import userController
from src.controller.myServiceController import myServiceController
from src.controller.myUnimoController import myUnimoController
from src.controller.settingsController import settingsController

# Load environment variables from .env
load_dotenv()

# Local Machine Path Structure
jsonValue = {}
if len(sys.argv) == 1:
    jsonValue = JsonReadService().readProfile('/src/profile/development_production.json')
elif sys.argv[1] == 'rakib':
    jsonValue = JsonReadService().readProfile('/home/myisland/temp/immiai/backend/Immican-api/src/profile'
                                             '/development_rakib.json')
elif sys.argv[1] == 'saminul':
    jsonValue = JsonReadService().readProfile('C:/Users/samin/immican/Immican-api/src/profile'
                                             '/development_saminul.json')
elif sys.argv[1] == 'yasir':
    jsonValue = JsonReadService().readProfile('C:/Users/gamer/Documents/immican/Immican-api/src/profile'
                                             '/development_yasir.json')
elif sys.argv[1] == 'production':
    jsonValue = JsonReadService().readProfile('Immican-api/src/profile/development_rakib.json')

# App Configuration
app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = jsonValue['DEBUG']
app.config['TESTING'] = jsonValue['TESTING']
app.config['ENV'] = jsonValue['ENV']
app.config['CSRF_ENABLED'] = jsonValue['CSRF_ENABLED']
app.config['PROPAGATE_EXCEPTIONS'] = jsonValue['PROPAGATE_EXCEPTIONS']
app.config['basedir'] = jsonValue['basedir']
app.config['SQLALCHEMY_ECHO'] = jsonValue['SQLALCHEMY_ECHO']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = jsonValue['SQLALCHEMY_TRACK_MODIFICATIONS']
app.config['SQLALCHEMY_POOL_SIZE'] = jsonValue['SQLALCHEMY_POOL_SIZE']
app.config['SQLALCHEMY_DATABASE_URI'] = jsonValue['SQLALCHEMY_DATABASE_URI']
app.config['fileUploadPath'] = jsonValue['fileUploadPath']


# JWT Configuration
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
jwt = JWTManager(app)


# API Slug Define For Every Controller
app.register_blueprint(loginController, url_prefix='/api/v1/login/')
app.register_blueprint(lookupController, url_prefix='/api/v1/lookup/')
app.register_blueprint(mailController, url_prefix='/api/v1/mail/')
app.register_blueprint(userController, url_prefix='/api/v1/user/')
app.register_blueprint(myServiceController, url_prefix='/api/v1/service/')
app.register_blueprint(myUnimoController, url_prefix='/api/v1/myunimo/')
app.register_blueprint(settingsController, url_prefix='/api/v1/settings/')

# sqlAlchemy and Marshmallow connect with the app
db.init_app(app)
ma.init_app(app)


@app.route('/')
@cross_origin()
def index():
    print('on index')
    return 'Python api Testing'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
