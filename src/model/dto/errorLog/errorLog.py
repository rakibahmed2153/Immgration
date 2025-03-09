from marshmallow import fields
from src.model.dto.dto import ma
import simplejson


class ErrorLogInformationDto(ma.Schema):
    id = fields.String()
    functions = fields.String(allow_none=True)
    errorMessage = fields.String(allow_none=True)
    url = fields.String(allow_none=True)
    createdDate = fields.DateTime(allow_none=True)

    class Meta:
        json_module = simplejson


class ErrorLogInformationAllDto(ma.Schema):
    id = fields.String(attribute="id")
    functions = fields.String(attribute='functions', allow_none=True)
    errorMessage = fields.String(attribute='error_message', allow_none=True)
    url = fields.String(attribute='url', allow_none=True)
    createdDate = fields.DateTime(attribute='created_date', allow_none=True)

    class Meta:
        json_module = simplejson
