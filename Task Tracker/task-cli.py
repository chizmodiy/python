import sys, json
from datetime import datetime

filename = 'Task Tracker\data.json'

def open_dump(data):
         with open(filename,'w') as obj:
                json.dump(data,obj)


#[1,2,3,4]
def enumerate_list(list):
    for index , x in enumerate(list):
         x['id'] = index
    return list
          
     


def main():
    # sys.argv[0] - це завжди назва самого файлу (calc.py)
    # sys.argv[1] - це буде наша команда (add, sub і т.д.)
    # sys.argv[2:] - це всі наступні дані
    tasks = []
    
    
    if len(sys.argv) < 2:
        print("Використання: python calc.py [команда] [числа]")
        return

    command = sys.argv[1] # Отримуємо команду

    # перевіряємо присутність файлу або створюємо пустий лист
    try :
        with open(filename) as obj:
            tasks = json.load(obj)
    except FileNotFoundError :
            with open(filename,'w') as obj:
                json.dump([],obj)
                tasks = []
    except json.decoder.JSONDecodeError:
            with open(filename,'w') as obj:
                json.dump([],obj)
                tasks= []

         
    if command == "add":
        # add "опис": Створює новий об'єкт, додає в список і зберігає файл.
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new= {
    "id": len(tasks) +1 ,
    "description": " ".join(sys.argv[2:]),
    "status": "todo", 
    "createdAt": time_now,
    "updatedAt": time_now
  }
        tasks.append(new)
        tasks = enumerate_list(tasks)
        open_dump(tasks)
        print(f"Output: Task added successfully (ID: {new['id']})")
                
    elif command == "update":
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #перевірили чи число  інт і склеєли нові дані
        try:
            id = int(sys.argv[2])
            new_description = " ".join(sys.argv[3:])
            #шукаємо те що потрібно замінити
            if id in [int(x['id']) for x in tasks]:     
                for x in tasks:
                    if x['id'] == id:
                        x['description'] = new_description
                        x['updatedAt'] = time_now
                        tasks = enumerate_list(tasks)
                        open_dump(tasks)
            else:
                print('Такого ід немає')
        except (IndexError, ValueError):
             print('Вхідні данні не вірні')
             sys.exit()

    elif command == "mark-in-progress":
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            #перевірили чи число  інт і склеєли нові дані
            try:
                id = int(sys.argv[2])
                new_status = 'in progress'
                #шукаємо те що потрібно замінити
                if id in [int(x['id']) for x in tasks]:     
                    for x in tasks:
                        if x['id'] == id:
                            x['status'] = new_status
                            x['updatedAt'] = time_now
                            tasks = enumerate_list(tasks)
                            open_dump(tasks)
                else:
                    print('Такого ід немає')
            except (IndexError, ValueError):
                print('Вхідні данні не вірні')
                sys.exit()

    elif command == "done":
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            #перевірили чи число  інт і склеєли нові дані
            try:
                id = int(sys.argv[2])
                new_status = 'done'
                #шукаємо те що потрібно замінити
                if id in [int(x['id']) for x in tasks]:     
                    for x in tasks:
                        if x['id'] == id:
                            x['status'] = new_status
                            x['updatedAt'] = time_now
                            tasks = enumerate_list(tasks)
                            open_dump(tasks)
                else:
                    print('Такого ід немає')
            except (IndexError, ValueError):
                print('Вхідні данні не вірні')
                sys.exit()

    elif command == "delete":
        try:
            id = int(sys.argv[2])
            #шукаємо те що потрібно замінити
            if id in [int(x['id']) for x in tasks]:     
                for x in tasks:
                    if x['id'] == id:
                        tasks. remove(x)
                tasks = enumerate_list(tasks)
                open_dump(tasks)
            else:
                print('Такого ід немає')
        except (IndexError, ValueError):
             print('Вхідні данні не вірні')
             sys.exit()

    elif command == 'list':
        try:
            type = sys.argv[2]
#task-cli list done
# task-cli list todo
# task-cli list in-progress
            if type == 'done':
                print("\nFull List\n")
                for x in tasks :
                    if x['status'] == 'done':
                        print(f"{x['id']}. {x['description']} - {x['status']}")
            elif type == "todo":
                print("\nFull List\n")
                for x in tasks :
                    if x['status'] == 'todo':
                        print(f"{x['id']}. {x['description']} - {x['status']}")
            elif type == "in-progress":
                print("\nFull List\n")
                for x in tasks :
                    if x['status'] == 'in-progress':
                        print(f"{x['id']}. {x['description']} - {x['status']}")
        except:
            print("\nFull List\n")
            for x in tasks:
                print(f"{x['id']}. {x['description']} - {x['status']}")
    else: 
        print(f"Невідома команда: {command}")

if __name__ == "__main__":
    main()