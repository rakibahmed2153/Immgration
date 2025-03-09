import uuid
from src.model.entity.entity import db


def generate_uuid():
    return str(uuid.uuid4())

class UploadDocuments(db.Model):
    __tablename__ = 'user_documents'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    userId = db.Column('user_id', db.String)
    documentName = db.Column('document_name', db.String, nullable=False)
    documentType = db.Column('document_type', db.String, nullable=False)
    documentSubType = db.Column('document_sub_type', db.String, nullable=True)
    contentType = db.Column('content_type', db.String, nullable=True)
    fileUrl = db.Column('file_url', db.String, nullable=True)
    uploadDate = db.Column('upload_date', db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, userId, documentName, documentType, documentSubType, contentType, fileUrl, uploadDate=None):
        self.userId = userId
        self.documentName = documentName
        self.documentType = documentType
        self.documentSubType = documentSubType
        self.contentType = contentType
        self.fileUrl = fileUrl
        self.uploadDate = uploadDate if uploadDate is not None else db.func.current_timestamp()
