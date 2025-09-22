"""
Service Package
"""

from flask import Flask
from service.common import log_handlers
from service import routes  # noqa: F401  # needed for route registration

app = Flask(__name__)

# Initialize logging
log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info(" SERVICE RUNNING ".center(70, "*"))
app.logger.info(70 * "*")
