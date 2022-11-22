def switch(tasks, completed, title =""):
    count = 0
    newDicc = {"total_items": 0, "data": [] }
    if completed.lower() == 'true' and not bool(title):
        for task in tasks:
            if task["completed"]:
                count += 1
                newDicc['data'].append(task)
        newDicc['total_items']= count
        return newDicc
    if completed.lower() == 'false' and not bool(title):
        print('entro ACA')
        for task in tasks:
            if not task["completed"]:
                count += 1
                newDicc['data'].append(task)
        newDicc['total_items']= count
        return newDicc
    if completed.lower() == 'false' and title:
        for task in tasks:
            if task["title"] == title and not task["completed"]:
                count += 1
                newDicc['data'].append(task)
        newDicc['total_items']= count
        return newDicc
    elif completed and title:
        for task in tasks:
            if task["completed"] and task["title"] == title:
                count += 1
                newDicc['data'].append(task)
        newDicc['total_items']= count
        return newDicc
    elif title:
        for task in tasks:
            if task["title"] == title:
                count += 1
                newDicc['data'].append(task)
        newDicc['total_items']= count
        return newDicc
    else:
        for task in tasks:
            count += 1
            newDicc['data'].append(task)
        newDicc['total_items']= count
        return newDicc