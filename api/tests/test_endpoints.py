from gae_base import GAEBaseTest

from mock import patch
from endpoints import BadRequestException
from handlers.fantasy_api import FantasyAPI


# @patch.object(mock_import, 'fetch_page_async', MockAsyncPage())
class TestFantasyEndpoints(GAEBaseTest):

    def setUp(self):
        super(TestFantasyEndpoints, self).setUp()
        self.api = FantasyAPI()

    def test_get_existing_request(self):
        request = FantasyAPI.create.remote.request_type(name="name")

        result = self.api.create(request)
        self.assertTrue(result.success, "Request Error: Get was not successful.")

    def test_request_fail(self):
        request = FantasyAPI.create.remote.request_type()
        with self.assertRaises(BadRequestException) as context:
            self.api.create(request)
        ex = context.exception
        self.assertEqual(400, ex.http_status)
        self.assertIn('Name Required', ex.message)
