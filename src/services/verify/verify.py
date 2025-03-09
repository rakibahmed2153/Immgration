from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def validateAccessToken():
    try:
        # The access token is valid if it reaches here
        print('valid user check')
        current_user = get_jwt_identity()
        print(current_user)

        return current_user
    except Exception as e:
        print('Error validating access token:', e)
        return ''
