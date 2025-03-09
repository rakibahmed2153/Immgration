from src.model.entity.entity import db
from sqlalchemy import text


def dataFetch(sql, type):
    try:
        print('Common DB Call')

        connection = db.engine.connect()
        if type == 'all':
            queryCall = connection.execute(text(sql)).fetchall()
        else:
            queryCall = connection.execute(text(sql)).fetchone()
        connection.close()

        # print('queryCall', queryCall)
        return queryCall

    except Exception as e:
        print('Exception', e)
        return []


def queryRun(sql):
    try:
        print('Common DB Call')

        connection = db.engine.connect()
        connection.execute(text(sql))
        connection.close()
        db.session.commit()

        # print('queryCall', queryCall)
        return True

    except Exception as e:
        print('Exception', e)
        return False
