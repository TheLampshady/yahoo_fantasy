import json

from gae_base import GAEBaseTest

from mock import patch

from clients.yahoo import YahooClient
from models.config import AuthAccount


# @patch.object(mock_import, 'process_user', lambda: "test@email.com")
class TestYahooClient(GAEBaseTest):

    def setUp(self):
        super(TestYahooClient, self).setUp()
        with open("yahoo_key.json") as f:
            AuthAccount.save_key("yahoo", json.loads(f.read()))
        self.assertTrue(AuthAccount.query().fetch())
        self.client = YahooClient.load_by_ndb()
        self.assertTrue(self.client.client_id)

    def test_yahoo_call(self):
        pass
