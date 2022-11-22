def get_user_and_tasks(tasks, user):
  # print(user)
  if user == 'Not found':
    return 'User not found'
  else:
    count = 0
    newDicc = {"total_items": 0, "data": []}
    if len(tasks['data']) > 0:
      for task in tasks['data']:
        if int(task['user_id']) == int(user['id']):
          count +=1
          newDicc['data'].append(task)
      newDicc['total_items'] = count
      return newDicc
    else:
      return newDicc