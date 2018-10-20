import logging
import os

from google.appengine.ext import vendor
from google.appengine.api import app_identity

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

cwd = os.path.dirname(os.path.abspath(__file__))
libs = os.path.join(cwd, "libs")
vendor.add(libs)

try:
    APPLICATION_ID = app_identity.get_application_id()
except Exception as e:
    APPLICATION_ID = "local"
SERVER_SOFTWARE = os.environ.get('SERVER_SOFTWARE', 'Unknown')
logger.info("Starting Application: %s" % APPLICATION_ID)
logger.info("SERVER_SOFTWARE: %s" % SERVER_SOFTWARE)

IS_LOCAL = SERVER_SOFTWARE.startswith('Dev') or SERVER_SOFTWARE == "Unknown"
logger.info("Local Mode: %s" % IS_LOCAL)
