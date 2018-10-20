import logging

import endpoints
from protorpc import message_types, remote


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@endpoints.api(
    name='task',
    version='v1',
    base_path='/api/',
)
class TaskAPI(remote.Service):

    @endpoints.method(path='auto', http_method='GET', name='auto')
    def auto(self, request):
        logging.info("Auto Ran")
        return message_types.VoidMessage()

