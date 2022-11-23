from flask import request, Blueprint
import json
from modules.get_by_id import get_by_id
from modules.switch import switch

routeTasks = Blueprint('routeTasks', __name__)

with open('./api/tasks.json', 'r') as file:
    tasks = json.load(file)

@routeTasks.route('/tasks', methods=['GET'])
def get_tasks():
    completed = request.args.get('completed')
    title = request.args.get('title')
    if not completed:
      completed = ""
    return switch(tasks, completed, title)

@routeTasks.route('/tasks/<int:id>', methods=['GET'])
def task_id(id):
  return get_by_id(id, tasks)
