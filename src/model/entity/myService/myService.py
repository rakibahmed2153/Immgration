import uuid
from src.model.entity.entity import db


def generate_uuid():
    return str(uuid.uuid4())


class MyServiceInformation(db.Model):
    __tablename__ = 'my_service'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    service = db.Column('service', db.String)
    categoryId = db.Column('category_id', db.String)
    subCategoryId = db.Column('sub_category_id', db.String)
    userId = db.Column('user_id', db.String)
    version = db.Column('version', db.String)
    createdDate = db.Column('created_date', db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, service, categoryId, subCategoryId, version, userId):
        self.service = service
        self.categoryId = categoryId
        self.subCategoryId = subCategoryId
        self.version = version
        self.userId = userId
        self.createdDate = db.func.current_timestamp()


class MyServiceDetailsInformation(db.Model):
    __tablename__ = 'my_service_details'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    serviceId = db.Column('service_id', db.String)
    labelName = db.Column('label_name', db.String)
    labelDetails = db.Column('label_details', db.Text)
    labelNo = db.Column('label_no', db.Integer)
    createdDate = db.Column('created_date', db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, serviceId, labelName, labelDetails, labelNo):
        self.serviceId = serviceId
        self.labelName = labelName
        self.labelDetails = labelDetails
        self.labelNo = labelNo
        self.createdDate = db.func.current_timestamp()
