import uuid
from src.model.entity.entity import db


def generate_uuid():
    return str(uuid.uuid4())


class LookupConfigureInformation(db.Model):

    __tablename__ = 'lookup_configure'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    lookupCode = db.Column('lookup_code', db.String)
    lookupName = db.Column('lookup_name', db.String)
    shortName = db.Column('short_name', db.String)
    lookupLevel = db.Column('lookup_level', db.String)
    lookupNote = db.Column('lookup_note', db.String)
    isActive = db.Column('is_active', db.Boolean)
    createdDate = db.Column('created_date', db.TIMESTAMP, server_default=db.func.current_timestamp())
    createdBy = db.Column('created_by', db.String(255))

    def __init__(self, lookupCode, lookupName, lookupLevel, lookupNote=None, shortName=None,
                 isActive=False, createdBy=None):
        self.lookupCode = lookupCode
        self.lookupName = lookupName
        self.shortName = shortName
        self.lookupLevel = lookupLevel
        self.isActive = isActive
        self.lookupNote = lookupNote
        self.createdDate = db.func.current_timestamp()
        self.createdBy = createdBy


class LookupDataInformation(db.Model):

    __tablename__ = 'lookup_data'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    lookConfigId = db.Column('look_config_id', db.String)
    levelId = db.Column('level_id', db.String)
    levelData = db.Column('level_data', db.String)
    parentId = db.Column('parent_id', db.String)
    levelUii = db.Column('level_uii', db.String)
    levelCode = db.Column('level_code', db.String)
    lookupCode = db.Column('lookup_code', db.String)
    shortName = db.Column('short_name', db.String)
    createdDate = db.Column('created_date', db.TIMESTAMP, server_default=db.func.current_timestamp())
    createdBy = db.Column('created_by', db.String(255))

    def __init__(self, lookConfigId, levelId, levelData, parentId=None, levelUii=None, levelCode=False,
                 lookupCode=None, shortName=None, createdBy=None):
        self.lookConfigId = lookConfigId
        self.levelId = levelId
        self.levelData = levelData
        self.parentId = parentId
        self.levelUii = levelUii
        self.levelCode = levelCode
        self.lookupCode = lookupCode
        self.shortName = shortName
        self.createdDate = db.func.current_timestamp()
        self.createdBy = createdBy


class LookupLevelInformation(db.Model):

    __tablename__ = 'lookup_level'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    lookConfigId = db.Column('look_config_id', db.String)
    levelName = db.Column('level_name', db.String)
    levelCode = db.Column('level_code', db.String)
    createdDate = db.Column('created_date', db.TIMESTAMP, server_default=db.func.current_timestamp())
    createdBy = db.Column('created_by', db.String(255))

    def __init__(self, lookConfigId, levelName, levelCode, createdBy=None):
        self.lookConfigId = lookConfigId
        self.levelName = levelName
        self.levelCode = levelCode
        self.createdDate = db.func.current_timestamp()
        self.createdBy = createdBy
