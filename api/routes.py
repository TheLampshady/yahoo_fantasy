import endpoints
from handlers import FantasyAPI, TaskAPI

# Protected by OAuth2
APPLICATION = endpoints.api_server([
    FantasyAPI,
])

# Protected by admin login
TASKS = endpoints.api_server([
    TaskAPI,
])
