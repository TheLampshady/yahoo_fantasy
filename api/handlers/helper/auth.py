import endpoints

from appengine_config import IS_LOCAL

LOCALHOST_CLIENT_ID = "..."
PROD_CLIENT_ID = "..."

ALLOWED_CLIENT_IDS = [
    endpoints.API_EXPLORER_CLIENT_ID,
    LOCALHOST_CLIENT_ID,
    PROD_CLIENT_ID
]
SCOPES = [endpoints.EMAIL_SCOPE]


def process_user():
    """
    :rtype: AdminUser
    """
    user = endpoints.get_current_user()
    if not user:
        raise endpoints.UnauthorizedException("Authentication required.")
    email = user.email().lower()
    return email

