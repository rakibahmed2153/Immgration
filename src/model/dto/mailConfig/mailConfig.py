import simplejson
from marshmallow import fields
from src.model.dto.dto import ma


# Mail Configure Dto
class MailConfigureDto(ma.Schema):
    id = fields.String()
    senderEmail = fields.String(allow_none=True)
    password = fields.String(allow_none=True)
    isActive = fields.Boolean(allow_none=True)
    subject = fields.String(allow_none=True)
    body = fields.String(allow_none=True)
    port = fields.Integer(allow_none=True)
    server = fields.String(allow_none=True)
    signature = fields.String(allow_none=True)
    key = fields.String(allow_none=True)
    mailFor = fields.String(allow_none=True)
    senderTitle = fields.String(allow_none=True)
    createdDate = fields.DateTime(allow_none=True)
    createdBy = fields.String(allow_none=True)

    class Meta:
        json_module = simplejson


# Mail Configure With Dto
class MailConfigureWithDto(ma.Schema):
    id = fields.String(attribute="id")
    senderEmail = fields.String(attribute="sender_email", allow_none=True)
    password = fields.String(attribute="password", allow_none=True)
    isActive = fields.Boolean(attribute="is_active", allow_none=True)
    subject = fields.String(attribute="subject", allow_none=True)
    body = fields.String(attribute="body", allow_none=True)
    signature = fields.String(attribute="signature", allow_none=True)
    port = fields.Integer(attribute="port", allow_none=True)
    server = fields.String(attribute="server", allow_none=True)
    key = fields.String(attribute="key", allow_none=True)
    mailFor = fields.String(attribute="mail_for", allow_none=True)
    senderTitle = fields.String(attribute="sender_title", allow_none=True)
    createdBy = fields.String(attribute="created-by", allow_none=True)
    createdDate = fields.DateTime(attribute="created_date", allow_none=True)

    class Meta:
        json_module = simplejson
