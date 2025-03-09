from marshmallow import fields
from src.model.dto.dto import ma
import simplejson


class LookupConfigureDto(ma.Schema):
    id = fields.String()
    lookupCode = fields.String(required=True)
    lookupName = fields.String(required=True)
    shortName = fields.String(allow_none=True)
    lookupLevel = fields.String(required=True)
    lookupNote = fields.String(allow_none=True)
    isActive = fields.Boolean(allow_none=True)
    createdBy = fields.String(allow_none=True)


class LookupConfigureDtoList(ma.Schema):
    id = fields.String(attribute="id", allow_none=True)
    lookupCode = fields.String(attribute="lookup_code", allow_none=True)
    lookupName = fields.String(attribute="lookup_name", allow_none=True)
    shortName = fields.String(attribute="short_name", allow_none=True)
    levelCode = fields.String(attribute="level_code", allow_none=True)
    lookupLevel = fields.String(attribute="lookup_level", required=True)
    lookupNote = fields.String(attribute="lookup_note", allow_none=True)
    isActive = fields.Boolean(attribute="is_active", allow_none=True)
    createdDate = fields.DateTime(attribute="created_date", allow_none=True)
    createdBy = fields.String(attribute="created_by", allow_none=True)

    class Meta:
        json_module = simplejson


class LookupDataDto(ma.Schema):
    id = fields.String()
    lookupConfigId = fields.String(required=True)
    levelId = fields.String(required=True)
    levelData = fields.String(required=True)
    parentId = fields.String(required=True)
    levelUii = fields.String(required=True)
    levelCode = fields.String(required=True)
    lookupCode = fields.String(required=True)
    shortName = fields.String(required=True)
    createdBy = fields.String(allow_none=True)


class LookupDataDtoList(ma.Schema):
    id = fields.String(attribute="id", allow_none=True)
    lookupConfigId = fields.String(attribute="lookup_config_id", allow_none=True)
    levelId = fields.String(attribute="level_id", allow_none=True)
    levelData = fields.String(attribute="level_data", allow_none=True)
    parentId = fields.String(attribute="parent_id", allow_none=True)
    levelUii = fields.String(attribute="level_uii", required=True)
    levelCode = fields.String(attribute="level_code", allow_none=True)
    lookupCode = fields.String(attribute="lookup_code", allow_none=True)
    shortName = fields.String(attribute="short_name", allow_none=True)
    createdDate = fields.DateTime(attribute="created_date", allow_none=True)
    createdBy = fields.String(attribute="created_by", allow_none=True)

    class Meta:
        json_module = simplejson


class LookupLevelDto(ma.Schema):
    id = fields.String()
    lookupConfigId = fields.String(required=True)
    levelName = fields.String(required=True)
    levelCode = fields.String(required=True)
    createdBy = fields.String(allow_none=True)


class LookupLevelDtoList(ma.Schema):
    id = fields.String(attribute="id", allow_none=True)
    lookupConfigId = fields.String(attribute="lookup_config_id", allow_none=True)
    levelName = fields.String(attribute="level_name", allow_none=True)
    levelCode = fields.String(attribute="level_code", allow_none=True)
    createdDate = fields.DateTime(attribute="created_date", allow_none=True)
    createdBy = fields.String(attribute="created_by", allow_none=True)

    class Meta:
        json_module = simplejson

