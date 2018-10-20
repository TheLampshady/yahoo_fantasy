import logging

from google.appengine.ext import ndb

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AuthAccount(ndb.Model):
    app_id = ndb.StringProperty()
    client_id = ndb.StringProperty()
    client_secret = ndb.StringProperty()

    @classmethod
    def get_key(cls, key):
        """
        :type key: str
        :rtype: AuthAccount
        """
        entry = cls.get_by_id(key)
        if entry:
            return entry
        cls(
            id=key,
            app_id="Fill Me Out.",
            client_id="Fill Me Out.",
            client_secret="Fill Me Out."
        ).put()
        raise LookupError("Please Enter OAuth Info into Application.")

    @classmethod
    def save_key(cls, key, props):
        cls(
            id=key,
            app_id=props.get("appId"),
            client_id=props.get("clientId"),
            client_secret=props.get("clientSecret")
        ).put()

    def to_dict(self):
        return dict(
            id=self.key.id(),
            app_id=self.app_id,
            client_id=self.client_id,
            client_secret=self.client_secret
        )
