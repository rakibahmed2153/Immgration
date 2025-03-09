import uuid
from src.model.entity.entity import db


def generate_uuid():
    return str(uuid.uuid4())


class PolicyDetails(db.Model):

    __tablename__ = 'policy_details'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    policyDetails = db.Column('policy_details', db.String)
    policyTypeId = db.Column('policy_type_id', db.String)
    createdBy = db.Column('created_by', db.String)
    createdDate = db.Column('created_date', db.TIMESTAMP, server_default=db.func.current_timestamp())
    updatedDate = db.Column('updated_date', db.TIMESTAMP, server_default=db.func.current_timestamp())
    lastUpdatedBy = db.Column('last_updated_by', db.String)

    def __init__(self, policyDetails, policyTypeId, createdBy, lastUpdatedBy):
        self.policyDetails = policyDetails
        self.policyTypeId = policyTypeId
        self.createdBy = createdBy
        self.lastUpdatedBy = lastUpdatedBy
        self.createdDate = db.func.current_timestamp()
        self.updatedDate = db.func.current_timestamp()