from src.model.entity.entity import db
# ======== Import Dto, Entity ===========
from src.services.sql.queryExecute import dataFetch
from src.model.entity.login.login import UsersLoginInformation, ImmigrantProfile


def immigrantDetails(userId):
    try:
        # print('userId', userId)
        and_clause = ["%s = '%s'" % ('ul.id', userId)]
        tableDetails = ("pp.id, pp.first_name, pp.last_name, pp.email, pp.phone, "
                        " pp.user_type, pp.about, pp.country_residence, pp.address, pp.twitter_profile,"
                        " pp.facebook_profile, pp.instagram_profile, pp.linkedin_profile, pp.profile_allow"
                        " from immigrant_profile pp left join users_login ul on ul.user_id=pp.id")
        and_clause_str = ' AND '.join(and_clause)
        sql_query = 'select ' + tableDetails + ' where ' + and_clause_str
        details = dataFetch(sql_query, 'one')
        return details

    except Exception as e:
        print('Immigrant Get Profile', e)


def immigrantDetailsUpdate(data, userId):
    try:
        print('data', userId)
        userId = UsersLoginInformation.query.filter_by(id=userId).first()
        print('userId', userId)
        db.session.query(ImmigrantProfile).filter_by(id=userId.userId).update({
            'firstName': data['firstName'],
            'lastName': data['lastName'],
            'email': data['email'],
            'phone': data['phone'],
            'about': data['about'],
            'countryResidence': data['countryResidence'],
            'address': data['address'],
            'twitterProfile': data['twitterProfile'],
            'facebookProfile': data['facebookProfile'],
            'instagramProfile': data['instagramProfile'],
            'linkedinProfile': data['linkedinProfile'],
        })
        db.session.commit()
        return {"type": True, "message": "Immigrant details update successful", "status": "success", "statusCode": 200}

    except Exception as e:
        print('Immigrant Get Profile', e)
        return {"type": False, "message": "Immigrant details update failed", "status": "failed", "statusCode": 201}


def allowImmigrantViewUpdate(data, userId):
    try:
        print('allowViewUpdate', data)
        userId = UsersLoginInformation.query.filter_by(id=userId).first()
        print('userId', userId)
        db.session.query(ImmigrantProfile).filter_by(id=userId.userId).update({
            'profileAllow': data['profileAllow'],
        })
        db.session.commit()
        return {"type": True, "message": "Allow profile view update successful", "status": "success", "statusCode": 200}

    except Exception as e:
        print('Immigrant Get Profile', e)
        return {"type": False, "message": "Immigrant details update failed", "status": "failed", "statusCode": 201}
