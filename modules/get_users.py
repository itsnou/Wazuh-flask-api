def all_users(users):
  total_numbers= 0
  newList = {"total_items": 0, "data": []}
  for user in users:
    total_numbers += 1
    newList['data'].append(user)
  newList['total_items'] = total_numbers
  return newList