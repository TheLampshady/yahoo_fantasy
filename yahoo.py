import base64
import requests
from urllib import urlencode
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

CLIENT_ID = "dj0yJmk9eE5qbzZVR0htbW1aJmQ9WVdrOU1VMDNUbVpyTlRBbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1kYQ--"
CLIENT_SECRET = "c76a31418320165d6bc6ea1477fb3a94664b5bbe"
TEST="ZGoweUptazllRTVxYnpaVlIwaHRiVzFhSm1ROVdWZHJPVTFWTUROVWJWcHlUbFJCYldOSGJ6bE5RUzB0Sm5NOVkyOXVjM1Z0WlhKelpXTnlaWFFtZUQxa1lRLS06Yzc2YTMxNDE4MzIwMTY1ZDZiYzZlYTE0NzdmYjNhOTQ2NjRiNWJiZQ=="

BASE_API = "https://api.login.yahoo.com"
TOKEN_URL = BASE_API + "/oauth/v2/get_token"
REQUEST_URL = BASE_API + "/oauth/v2/get_request_token"
AUTH_URL = BASE_API + "/oauth2/request_auth"
CODE = "ppm4c95"


def get_auth_params(client_id):
    return dict(
        client_id=client_id,
        redirect_uri="oob",
        response_type="code",
        language="en-us",
    )


def get_token_params2(client_id, client_secret, code):
    return dict(
        client_id=client_id,
        client_secret=client_secret,
        code=code,
        redirect_uri="oob",
        grant_type="authorization_code",
    )


def get_token_data(code):
    return dict(
        code=code,
        redirect_uri="oob",
        grant_type="authorization_code",
    )

def get_token_header(client_id, client_secret):
    client_code = "%s:%s" % (client_id, client_secret)
    auth = base64.b64encode(client_code)
    return {
        "Authorization": 'Basic {}'.format(auth),
        "Content-Type": "application/x-www-form-urlencoded"
    }

def run():
    params = get_auth_params(CLIENT_ID)
    params[''] = CLIENT_ID
    url = AUTH_URL + "?" + urlencode(params)
    # r = requests.get(AUTH_URL, params=params)
    headers = get_token_header(CLIENT_ID, CLIENT_SECRET)
    data = get_token_data(CODE)
    r = requests.post(TOKEN_URL, headers=headers, params=data)
    client = BackendApplicationClient(client_id=CLIENT_ID)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=TOKEN_URL, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    print token

if __name__ == "__main__":
    run()
