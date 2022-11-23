from flask import request, Blueprint
import json
from modules.get_by_id import get_by_id
from modules.switch import switch
from modules.get_users import all_users
from modules.get_user_and_tasks import get_user_and_tasks

routeUsers = Blueprint('routeUsers', __name__)

with open('./api/tasks.json', 'r') as file:
    tasks = json.load(file)

with open('./api/users.json', 'r') as file:
    users = json.load(file)


@routeUsers.route('/users', methods=['GET'])
def get_users():
  return all_users(users)

@routeUsers.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
  return get_by_id(user_id, users)

@routeUsers.route('/users/<int:user_id>/tasks')
def get_user_tasks(user_id):
  completed = request.args.get('completed')
  title = request.args.get('title')
  if not completed:
    completed = ""
  tasks_found = switch(tasks, completed, title)
  user_found = get_by_id(user_id, users)
  return get_user_and_tasks(tasks_found, user_found)
