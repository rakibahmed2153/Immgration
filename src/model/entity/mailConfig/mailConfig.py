import uuid
from src.model.entity.entity import db


def generate_uuid():
    return str(uuid.uuid4())


class MailConfigureInfo(db.Model):
    __tablename__ = 'mail_configuration'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    isActive = db.Column('is_active', db.Boolean)
    senderEmail = db.Column('sender_email', db.String)
    subject = db.Column('subject', db.String)
    body = db.Column('body', db.String)
    signature = db.Column('signature', db.String)
    password = db.Column('password', db.String)
    port = db.Column('port', db.Integer)
    server = db.Column('server', db.String)
    key = db.Column('key', db.String)
    mailFor = db.Column('mail_for', db.String)
    senderTitle = db.Column('sender_title', db.String)
    createdBy = db.Column('created_by', db.String(255))
    createdDate = db.Column('created_date', db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, senderEmail, isActive, subject, body, signature, password, port, senderTitle,
                 server, key, mailFor, createdBy=None):
        self.senderEmail = senderEmail
        self.isActive = isActive
        self.subject = subject
        self.body = body
        self.signature = signature
        self.password = password
        self.port = port
        self.server = server
        self.key = key
        self.senderTitle = senderTitle
        self.mailFor = mailFor
        self.createdBy = createdBy
        self.createdDate = db.func.current_timestamp()
