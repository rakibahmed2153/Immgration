import simplejson
from marshmallow import fields
from src.model.dto.dto import ma


# UploadDocuments Dto
class UploadDocumentsDto(ma.Schema):
    id = fields.String()
    userId = fields.String(allow_none=True)
    documentName = fields.String(allow_none=True)
    documentType = fields.String(allow_none=True)
    documentSubType = fields.String(allow_none=True)
    documentData = fields.Raw(allow_none=True)
    contentType = fields.String(allow_none=True)
    storyPath = fields.String(allow_none=True)
    uploadDate = fields.DateTime(allow_none=True)

    class Meta:
        json_module = simplejson


# UploadDocuments List
# class UploadDocumentsDtoList(ma.Schema):
#     id = fields.String(attribute="id")
#     userId = fields.String(attribute="user_id", allow_none=True)
#     documentName = fields.String(attribute="document_name", allow_none=True)
#     documentType = fields.String(attribute="document_type", allow_none=True)
#     documentSubType = fields.String(attribute="document_sub_type", allow_none=True)
#     documentData = fields.Raw(attribute="document_data", allow_none=True)
#     uploadDate = fields.DateTime(attribute="upload_date", allow_none=True)

#     class Meta:
#         json_module = simplejson
class UploadDocumentsDtoList(ma.Schema):
    id = fields.String(attribute="id")
    userId = fields.String(attribute="user_id", allow_none=True)
    documentName = fields.String(attribute="document_name", allow_none=True)
    documentType = fields.String(attribute="document_type", allow_none=True)
    documentSubType = fields.String(attribute="document_sub_type", allow_none=True)
    documentData = fields.Raw(attribute="document_data", allow_none=True)
    contentType = fields.String(attribute="content_type", allow_none=True)
    storyPath = fields.String(attribute="story_path", allow_none=True)
    uploadDate = fields.DateTime(attribute="upload_date", allow_none=True)
    fileUrl = fields.String(attribute="file_url", allow_none=True)

    class Meta:
        json_module = simplejson

