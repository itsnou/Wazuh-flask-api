from flask import Flask, request
import json
from modules.switch import switch
from modules.get_by_id import get_by_id
from modules.get_users import all_users
from modules.get_user_and_tasks import get_user_and_tasks
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
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

with open('./api/tasks.json', 'r') as file:
    tasks = json.load(file)

with open('./api/users.json', 'r') as file:
    users = json.load(file)

@app.route('/tasks', methods=['GET'])
def get_tasks():
  completed = request.args.get('completed')
  title = request.args.get('title')
  if not completed:
    completed = ""
  return switch(tasks, completed, title)

@app.route('/tasks/<int:id>', methods=['GET'])
def task_id(id):
  return get_by_id(id, tasks)

@app.route('/users', methods=['GET'])
def get_users():
  return all_users(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
  return get_by_id(user_id, users)

@app.route('/uses/<int:user_id>/tasks')
def get_user_tasks(user_id):
  completed = request.args.get('completed')
  title = request.args.get('title')
  if not completed:
    completed = ""
  tasks_found = switch(tasks, completed, title)
  user_found = get_by_id(user_id, users)
  return get_user_and_tasks(tasks_found, user_found)

