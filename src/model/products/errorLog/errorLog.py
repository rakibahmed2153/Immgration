# ======== Import Dto, Entity ===========
from src.model.entity.errorLog.errorLog import *
from src.model.dto.errorLog.errorLog import *

errorLogInformationDto = ErrorLogInformationDto()


def errorLogSave(url, functions, errorMessage):
    try:
        print('error log called...', errorMessage, url)

        errorInformation = ErrorLogInformation(errorMessage=errorMessage, functions=functions, url=url)
        db.session.add(errorInformation)
        db.session.commit()
        result = errorLogInformationDto.dump(errorInformation).data
        db.session.rollback()

        return "success"

    except Exception as e:
        print('e', e)
        return "failed"
