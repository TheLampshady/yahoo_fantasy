import logging
import os
import unittest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def tearDown(self):
        super(BaseTest, self).tearDown()


    @staticmethod
    def open(name='page.html'):
        cwd = os.getcwd()
        if os.path.basename(cwd) != "tests":
            cwd = os.path.join(cwd, "tests")
        mock_dir = os.path.join(cwd, "mock_data")

        filename = os.path.join(mock_dir, name)

        with open(filename, 'r') as f:
            content = f.read()
        return content
