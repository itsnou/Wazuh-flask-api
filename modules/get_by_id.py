def get_by_id(id, list):
  dicc_found = {}
  for dic in list:
    if dic['id'] == id:
      dicc_found = dic
  if dicc_found:
    return dicc_found
  else:
    return 'Not found'