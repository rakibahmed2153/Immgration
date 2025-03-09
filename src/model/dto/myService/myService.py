import simplejson
from marshmallow import fields
from src.model.dto.dto import ma


# My Service Dto
class MyServiceDto(ma.Schema):
    id = fields.String()
    service = fields.String(allow_none=True)
    categoryId = fields.String(allow_none=True)
    subCategoryId = fields.String(allow_none=True)
    version = fields.String(allow_none=True)
    userId = fields.String(allow_none=True)
    createdDate = fields.DateTime(allow_none=True)

    class Meta:
        json_module = simplejson


# My Service Dto List
class MyServiceDtoList(ma.Schema):
    id = fields.String(attribute="id")
    service = fields.String(attribute="service", allow_none=True)
    categoryId = fields.String(attribute="category_id", allow_none=True)
    categoryName = fields.String(attribute="category_name", allow_none=True)
    subCategoryId = fields.String(attribute="sub_category_id", allow_none=True)
    subCategoryName = fields.String(attribute="sub_category_name", allow_none=True)
    version = fields.String(attribute="version", allow_none=True)
    labelNo = fields.Integer(attribute="label_no", allow_none=True)
    userId = fields.String(attribute="user_id", allow_none=True)
    createdDate = fields.DateTime(attribute="created_date", allow_none=True)

    class Meta:
        json_module = simplejson


# My Service Details sDto
class MyServiceDetailsDto(ma.Schema):
    id = fields.String()
    serviceId = fields.String(allow_none=True)
    labelName = fields.String(allow_none=True)
    labelDetails = fields.String(allow_none=True)
    labelNo = fields.Integer(allow_none=True)
    createdDate = fields.DateTime(allow_none=True)

    class Meta:
        json_module = simplejson


# My Service Details Dto List
class MyServiceDetailsDtoList(ma.Schema):
    id = fields.String(attribute="id")
    serviceId = fields.String(attribute="service_id", allow_none=True)
    labelName = fields.String(attribute="label_name", allow_none=True)
    labelDetails = fields.String(attribute="label_details", allow_none=True)
    labelNo = fields.String(attribute="label_no", allow_none=True)
    createdDate = fields.DateTime(attribute="created_date", allow_none=True)

    class Meta:
        json_module = simplejson
