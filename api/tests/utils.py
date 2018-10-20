from io import open
import os
from urlparse import urlparse

from google.appengine.ext import ndb


class MockBasePage(object):
    def __init__(self):
        cwd = os.getcwd()
        if os.path.basename(cwd) != "tests":
            cwd = os.path.join(cwd, "tests")
        self.mock_dir = os.path.join(cwd, "mock_data")

    def get_content(self, url):
        ext = os.path.splitext(urlparse(url).path)[1].strip(".")
        name = 'page.html'
        clean_url = urlparse(url).path.strip('/')
        encoding = 'utf-8'

        if ext in ['css', 'js']:
            name = 'page.' + ext
        elif ext in ['jpeg', 'png', 'bmp', 'svg', 'gif', 'jpg']:
            name = 'page.png'
            encoding = "ISO-8859-1"
        elif clean_url:
            if clean_url.endswith("empty"):
                return None
            name = clean_url
        filename = os.path.join(self.mock_dir, name)

        with open(filename, 'r', encoding=encoding) as f:
            content = f.read()
        return content


class MockPage(MockBasePage):

    def __call__(self, url):
        return self.get_content(url)


class MockAsyncPage(MockBasePage):

    @ndb.tasklet
    def __call__(self, url):
        raise ndb.Return(self.get_content(url))
