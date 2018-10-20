import logging

import endpoints
from protorpc import message_types
from protorpc import messages
from protorpc import remote

from handlers.helper.auth import ALLOWED_CLIENT_IDS, SCOPES, process_user
from handlers.helper.extra import ListField, JsonField

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# [START messages]
class Result(messages.Message):
    success = messages.BooleanField(1)
    result = JsonField(2)


class Request(messages.Message):
    name = messages.StringField(1)


# [START resources]
CREATE_RESOURCE = endpoints.ResourceContainer(
    Request
)

ID_RESOURCE = endpoints.ResourceContainer(
    message_types.VoidMessage,
    id=messages.StringField(1, variant=messages.Variant.STRING, required=True)
)


@endpoints.api(
    name='fantasy',
    version='v1',
    base_path='/api/',
    scopes=SCOPES,
    allowed_client_ids=ALLOWED_CLIENT_IDS
)
class FantasyAPI(remote.Service):

    @endpoints.method(CREATE_RESOURCE, Result,
                      path='create', http_method='POST', name='create')
    def create(self, request):
        user = process_user()
        if not request.name:
            raise endpoints.BadRequestException("Name Required.")
        result = dict(
            success=True,
            data=dict()
        )
        return Result(**result)
