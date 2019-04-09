import tokenlib

def validate_token(token):
    try:
        tokenlib.parse_token(token, secret="AUTH_SERVER")
    except Exception, e:
        logging.error('Failed parse token: ' + str(e))
        return False
    return True

def create_token(username):
    return tokenlib.make_token({"username": auth.username}, secret="AUTH_SERVER")
