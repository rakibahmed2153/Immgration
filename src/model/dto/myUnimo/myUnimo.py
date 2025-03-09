import simplejson
from marshmallow import fields
from src.model.dto.dto import ma


# My Service Dto
class MyUnimoClientDetailsDto(ma.Schema):
    id = fields.String()
    # myUnimoNo = fields.Integer(allow_none=True)
    userId = fields.String(allow_none=True)
    serviceName = fields.String(allow_none=True)
    serviceId = fields.String(allow_none=True)
    serviceStepsId = fields.String(allow_none=True)
    clientEmail = fields.String(allow_none=True)
    clientPortalLink = fields.String(allow_none=True)
    meetingLink = fields.String(allow_none=True)
    requestStatus = fields.String(allow_none=True)
    customerStatus = fields.String(allow_none=True)
    discoverCallDate = fields.DateTime(allow_none=True)
    createdDate = fields.DateTime(allow_none=True)
    phone = fields.String(allow_none=True)
    firstName = fields.String(allow_none=True)
    lastName = fields.String(allow_none=True)
    stepNo = fields.Integer(allow_none=True)
    employeeName = fields.String(allow_none=True)
    currentClientStatus = fields.String(allow_none=True)
    currentClient = fields.Boolean(allow_none=True)

    class Meta:
        json_module = simplejson


# My Service Dto List
class MyUnimoClientDetailsDtoList(ma.Schema):
    id = fields.String(attribute="id")
    myUnimoNo = fields.Integer(attribute="my_unimo_no", allow_none=True)
    userId = fields.String(attribute="user_id", allow_none=True)
    serviceName = fields.String(attribute="service_name", allow_none=True)
    serviceId = fields.String(attribute="service_id", allow_none=True)
    serviceStepsId = fields.String(attribute="service_steps_id", allow_none=True)
    clientEmail = fields.String(attribute="client_email", allow_none=True)
    clientPortalLink = fields.String(attribute="client_portal_link", allow_none=True)
    meetingLink = fields.String(attribute="meeting_link", allow_none=True)
    requestStatus = fields.String(attribute="request_status", allow_none=True)
    customerStatus = fields.String(attribute="customer_status", allow_none=True)
    phone = fields.String(attribute="phone", allow_none=True)
    firstName = fields.String(attribute="first_name", allow_none=True)
    lastName = fields.String(attribute="last_name", allow_none=True)
    discoverCallDate = fields.DateTime(attribute="discover_call_date", allow_none=True)
    createdDate = fields.DateTime(attribute="created_date", allow_none=True)
    stepNo = fields.Integer(attribute="step_no", allow_none=True)
    employeeName = fields.String(attribute="employee_name", allow_none=True)
    email = fields.String(attribute="email", allow_none=True)
    currentClient = fields.Boolean(attribute="current_client", allow_none=True)
    currentClientStatus = fields.String(attribute="current_client_status", allow_none=True)
    labelDetails = fields.String(attribute="label_details", allow_none=True)
    labelName = fields.String(attribute="label_name", allow_none=True)
    end = fields.DateTime(attribute="end_date", allow_none=True)
    start = fields.DateTime(attribute="start_date", allow_none=True)
    title = fields.String(attribute="title", allow_none=True)
    clientId = fields.String(attribute="client_id", allow_none=True)

    class Meta:
        json_module = simplejson


class MyUnimoClientDetailsHistoryDto(ma.Schema):
    id = fields.String()
    # myUnimoNo = fields.Integer(allow_none=True)
    userId = fields.String(allow_none=True)
    serviceName = fields.String(allow_none=True)
    serviceId = fields.String(allow_none=True)
    serviceStepsId = fields.String(allow_none=True)
    clientEmail = fields.String(allow_none=True)
    clientPortalLink = fields.String(allow_none=True)
    requestStatus = fields.String(allow_none=True)
    customerStatus = fields.String(allow_none=True)
    discoverCallDate = fields.DateTime(allow_none=True)
    createdDate = fields.DateTime(allow_none=True)
    phone = fields.String(allow_none=True)
    firstName = fields.String(allow_none=True)
    lastName = fields.String(allow_none=True)
    stepNo = fields.Integer(allow_none=True)
    employeeName = fields.String(allow_none=True)
    currentClientStatus = fields.String(allow_none=True)
    currentClient = fields.Boolean(allow_none=True)

    class Meta:
        json_module = simplejson


# My Service Dto List
class MyUnimoClientDetailsHistoryDtoList(ma.Schema):
    id = fields.String(attribute="id")
    myUnimoNo = fields.Integer(attribute="my_unimo_no", allow_none=True)
    userId = fields.String(attribute="user_id", allow_none=True)
    serviceName = fields.String(attribute="service_name", allow_none=True)
    serviceId = fields.String(attribute="service_id", allow_none=True)
    serviceStepsId = fields.String(attribute="service_steps_id", allow_none=True)
    clientEmail = fields.String(attribute="client_email", allow_none=True)
    clientPortalLink = fields.String(attribute="client_portal_link", allow_none=True)
    requestStatus = fields.String(attribute="request_status", allow_none=True)
    customerStatus = fields.String(attribute="customer_status", allow_none=True)
    phone = fields.String(attribute="phone", allow_none=True)
    firstName = fields.String(attribute="first_name", allow_none=True)
    lastName = fields.String(attribute="last_name", allow_none=True)
    discoverCallDate = fields.DateTime(attribute="discover_call_date", allow_none=True)
    createdDate = fields.DateTime(attribute="created_date", allow_none=True)
    stepNo = fields.Integer(attribute="step_no", allow_none=True)
    employeeName = fields.String(attribute="employee_name", allow_none=True)
    email = fields.String(attribute="email", allow_none=True)
    currentClient = fields.Boolean(attribute="current_client", allow_none=True)
    currentClientStatus = fields.String(attribute="current_client_status", allow_none=True)

    class Meta:
        json_module = simplejson