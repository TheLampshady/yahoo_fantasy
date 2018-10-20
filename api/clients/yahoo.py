from models.config import AuthAccount


class YahooClient(object):

    BASE_URL = "https://fantasysports.yahooapis.com/fantasy/v2"
    DEFAULT_PARAMS = dict(
            format="json"
        )

    def __init__(self, app_id, client_id, client_secret):
        self.app_id = app_id
        self.client_id = client_id
        self.client_secret = client_secret

    @classmethod
    def load_by_ndb(cls):
        config = AuthAccount.get_key("yahoo").to_dict()
        return cls(
            config.get("app_id"),
            config.get("client_id"),
            config.get("client_secret")
        )

    def fetch(self):
        pass
