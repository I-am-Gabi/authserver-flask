import tokenlib

def token_refresh(token): 
    if validate_token(token):
        return token
    else:
        token = create_token(session.get('username')) 
        return token

def validate_token(token): 
    try:
        tokenlib.parse_token(token, secret="AUTH_SERVER")
    except Exception, e: 
        return e
    return True

def create_token(username):
    return tokenlib.make_token({"username": auth.username}, secret="AUTH_SERVER")

def save_token(token):
    id = None
    data = tokenlib.parse_token(token, secret="AUTH_SERVER")
    data_token = {
        "key": token,
        "expires": data['expires'],
        "username": data['username'],
        "salt": data['salt']
    } 
    return data_token
