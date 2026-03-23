x = [{"id": 5, "description": ["Hello"], "status": "todo", "createdAt": "2026-03-23 18:05:47", "updatedAt": "2026-03-23 18:05:47"}, {"id": 6, "description": ["Hell22"], "status": "todo", "createdAt": "2026-03-23 18:06:09", "updatedAt": "2026-03-23 18:06:09"}, {"id": 3, "description": ["Hell33"], "status": "todo", "createdAt": "2026-03-23 18:07:12", "updatedAt": "2026-03-23 18:07:12"}]

def enumerate_list(list):
    for index , x in enumerate(list):
         x['id'] = index
    x = list

enumerate_list(x)
    