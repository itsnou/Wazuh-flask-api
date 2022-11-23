from flask import Flask, request
import json
from modules.switch import switch
from modules.get_by_id import get_by_id
from modules.get_users import all_users
from modules.get_user_and_tasks import get_user_and_tasks
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from routes.tasks import routeTasks
from routes.users import routeUsers

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

SWAGGER_URL = '/docs'
API_URL = "../static/swagger.json"

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Test application"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(routeTasks)
app.register_blueprint(routeUsers)
