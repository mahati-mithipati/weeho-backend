import taskiq_fastapi
from taskiq import InMemoryBroker, ZeroMQBroker

from weeho_backend.settings import settings

broker = (
    InMemoryBroker() if settings.environment.lower() == "pytest" else ZeroMQBroker()
)

taskiq_fastapi.init(
    broker,
    "weeho_backend.web.application:get_app",
)
