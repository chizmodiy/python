import json
filename = "Daily Task Tracker/tasks.json"

class Task:
    """Має назву, пріоритет (Low, Medium, High) та статус (Done/Not Done)."""
    def __init__(self,name,priority,status):
        self.name = name
        self.priority = priority
        self.status = status
    
class ToDoManager():
    def __init__(self):
        self.tasks = []
        try :
            with open(filename) as obj:
                self.tasks = json.load(obj)
        except FileNotFoundError :
            with open(filename,'w') as obj:
                json.dump([],obj)
                self.tasks = []
        except json.decoder.JSONDecodeError:
            with open(filename,'w') as obj:
                json.dump([],obj)
                self.tasks= []    
     

    def add_task(self, name, priority):
        new_task = Task(name,priority,'Not Done')
        self.tasks.append(new_task.__dict__)
        


    def show_tasks(self):
        for x in enumerate(self.tasks):
            print(x)

    def mark_as_done(self, task_index):
        if task_index in [x for x in range(0,len(self.tasks))]:
            if self.tasks[task_index]['status'] == 'Done':
                print('This status is Done now')
            elif self.tasks[task_index]['status'] == 'Not Done':
                self.tasks[task_index]['status'] = 'Done'
                with open(filename,'w') as fl_obj:
                    json.dump(self.tasks,fl_obj)
                print('You update this status  - Done now')
        else:
            print('This index is out of range')

    def mark_as_undone(self, task_index):
        if task_index in [x for x in range(0,len(self.tasks))]:
            if self.tasks[task_index]['status'] == 'Not Done':
                print('This status is Not Done now')
            elif self.tasks[task_index]['status'] == 'Done':
                self.tasks[task_index]['status'] = 'Not Done'
                with open(filename,'w') as fl_obj:
                    json.dump(self.tasks,fl_obj)
                print('You update this status  - Not Done now')
        else:
            print('This index is out of range')
    def clear_completed(self):
        compleatly_list = [x for x in self.tasks if x['status'] == "Done"]
        self.tasks = compleatly_list
        with open(filename,'w') as fl_obj:
                    json.dump(self.tasks,fl_obj)
        print("Dict is succsesully clear")

        


inicialize = ToDoManager()
inicialize.add_task('book','Low')
inicialize.add_task('book','Low')
inicialize.add_task('book','Low')
inicialize.add_task('book','Low')
inicialize.show_tasks()
inicialize.mark_as_done(1)
inicialize.show_tasks()
inicialize.clear_completed()
inicialize.show_tasks()


               
        