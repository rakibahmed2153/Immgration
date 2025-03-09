import uuid
from src.model.entity.entity import db


def generate_uuid():
    return str(uuid.uuid4())


class MyUnimoClientDetails(db.Model):

    __tablename__ = 'my_unimo_client_details'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    # myUnimoNo = db.Column('my_unimo_no', db.Integer)
    serviceName = db.Column('service_name', db.String)
    serviceId = db.Column('service_id', db.String)
    serviceStepsId = db.Column('service_steps_id', db.String)
    clientEmail = db.Column('client_email', db.String)
    clientPortalLink = db.Column('client_portal_link', db.String)
    meetingLink = db.Column('meeting_link', db.String)
    requestStatus = db.Column('request_status', db.String)
    customerStatus = db.Column('customer_status', db.String)
    discoverCallDate = db.Column('discover_call_date', db.TIMESTAMP)
    userId = db.Column('user_id', db.String)
    token = db.Column('token', db.String)
    phone = db.Column('phone', db.String)
    firstName = db.Column('first_name', db.String)
    lastName = db.Column('last_name', db.String)
    stepNo = db.Column('step_no', db.Integer)
    employeeName = db.Column('employee_name', db.String)
    currentClient = db.Column('current_client', db.Boolean)
    currentClientStatus = db.Column('current_client_status', db.String)
    createdDate = db.Column('created_date', db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, userId, serviceName, serviceId, serviceStepsId, clientEmail, clientPortalLink=None,
                 requestStatus='! Pending', customerStatus='Requested', discoverCallDate=None, token=None,
                 phone=None, firstName=None, lastName=None, employeeName=None, stepNo=0, currentClient=False,
                 currentClientStatus=None, meetingLink=None):
        # self.myUnimoNo = myUnimoNo
        self.userId = userId
        self.serviceName = serviceName
        self.serviceId = serviceId
        self.serviceStepsId = serviceStepsId
        self.clientEmail = clientEmail
        self.clientPortalLink = clientPortalLink
        self.requestStatus = requestStatus
        self.customerStatus = customerStatus
        self.discoverCallDate = discoverCallDate
        self.currentClientStatus = currentClientStatus
        self.token = token
        self.phone = phone
        self.firstName = firstName
        self.lastName = lastName
        self.employeeName = employeeName
        self.stepNo = stepNo
        self.currentClient = currentClient
        self.meetingLink = meetingLink
        self.createdDate = db.func.current_timestamp()


class MyUnimoClientDetailsHistory(db.Model):

    __tablename__ = 'my_unimo_client_details_history'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    # myUnimoNo = db.Column('my_unimo_no', db.Integer)
    serviceName = db.Column('service_name', db.String)
    serviceId = db.Column('service_id', db.String)
    serviceStepsId = db.Column('service_steps_id', db.String)
    clientEmail = db.Column('client_email', db.String)
    clientPortalLink = db.Column('client_portal_link', db.String)
    requestStatus = db.Column('request_status', db.String)
    customerStatus = db.Column('customer_status', db.String)
    discoverCallDate = db.Column('discover_call_date', db.TIMESTAMP)
    userId = db.Column('user_id', db.String)
    phone = db.Column('phone', db.String)
    firstName = db.Column('first_name', db.String)
    lastName = db.Column('last_name', db.String)
    stepNo = db.Column('step_no', db.Integer)
    employeeName = db.Column('employee_name', db.String)
    currentClient = db.Column('current_client', db.Boolean)
    currentClientStatus = db.Column('current_client_status', db.String)
    createdDate = db.Column('created_date', db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, userId, serviceName, serviceId, serviceStepsId, clientEmail, clientPortalLink=None,
                 requestStatus='! Pending', customerStatus='Requested', discoverCallDate=None,
                 phone=None, firstName=None, lastName=None, employeeName=None, stepNo=0, currentClient=False,
                 currentClientStatus=None):
        # self.myUnimoNo = myUnimoNo
        self.userId = userId
        self.serviceName = serviceName
        self.serviceId = serviceId
        self.serviceStepsId = serviceStepsId
        self.clientEmail = clientEmail
        self.clientPortalLink = clientPortalLink
        self.requestStatus = requestStatus
        self.customerStatus = customerStatus
        self.discoverCallDate = discoverCallDate
        self.currentClientStatus = currentClientStatus
        self.phone = phone
        self.firstName = firstName
        self.lastName = lastName
        self.employeeName = employeeName
        self.stepNo = stepNo
        self.currentClient = currentClient
        self.createdDate = db.func.current_timestamp()