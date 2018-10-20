import logging
import unittest

from base import BaseTest

from google.appengine.ext import testbed, ndb
from google.appengine.ext import vendor

vendor.add('libs')


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DEFAULT_BUCKET = "app_default_bucket"


class GAEBaseTest(BaseTest):

    def setUp(self):
        super(GAEBaseTest, self).setUp()
        self.init_testbed()
        ndb.get_context().clear_cache()

    def init_testbed(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()

        # add in services we will be testing
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_logservice_stub()
        self.testbed.init_urlfetch_stub()

        # For cloudstorage
        self.testbed.init_app_identity_stub()
        self.testbed.init_blobstore_stub()

    def tearDown(self):
        super(GAEBaseTest, self).tearDown()
        self.testbed.deactivate()

