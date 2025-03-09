import simplejson
from marshmallow import fields
from src.model.dto.dto import ma


#Policy Details
class PolicyDetailsDto(ma.Schema):
    id = fields.String()
    policyDetails = fields.String(allow_none=True)
    policyTypeId = fields.String(allow_none=True)
    createdBy = fields.String(allow_none=True)
    createdDate = fields.DateTime(allow_none=True)
    updatedDate = fields.DateTime(allow_none=True)
    lastUpdatedBy = fields.String(allow_none=True)

    class Meta:
        json_module = simplejson


# Policy Details Dto List
class PolicyDetailsDtoList(ma.Schema):
    id = fields.String(attribute="id")
    policyDetails = fields.String(attribute="policy_details", allow_none=True)
    policyTypeId = fields.String(attribute="policy_type_id", allow_none=True)
    policyTypeName = fields.String(attribute="policy_type_name", allow_none=True)
    createdBy = fields.String(attribute="created_by", allow_none=True)
    createdDate = fields.DateTime(attribute="created_date", allow_none=True)
    updatedDate = fields.DateTime(attribute="updated_date", allow_none=True)
    lastUpdatedBy = fields.String(attribute="last_updated_by", allow_none=True)

    class Meta:
        json_module = simplejson