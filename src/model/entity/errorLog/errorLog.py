import uuid
from src.model.entity.entity import db


def generate_uuid():
    return str(uuid.uuid4())


class ErrorLogInformation(db.Model):

    __tablename__ = 'error_log'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    functions = db.Column("functions", db.String)
    url = db.Column("url", db.String)
    errorMessage = db.Column("error_message", db.String)
    createdDate = db.Column('created_date', db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, errorMessage, functions=None, url=None):
        self.functions = functions
        self.errorMessage = errorMessage
        self.url = url
        self.createdDate = db.func.current_timestamp()
