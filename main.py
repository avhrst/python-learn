from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


my_tasks = []

class Task(BaseModel):
    id: int
    title: str
    description: str
    
def get_id():
    return my_tasks[-1].id + 1 if my_tasks else 1
 
def create_tasks(task: Task):
    task.id = get_id()
    my_tasks.append(task)
    return task 

def get_tasks():
    return my_tasks

def get_task_by_id(id: int):
    for task in my_tasks:
        if task.id == id:
            return task
    return None

def update_tasks(id: int, task: Task):
    for i, n in enumerate(my_tasks):
        if n.id == id:
            my_tasks[i] = task
            return task
    return None 
 
def delete_tasks(id: int):
    for i, task in enumerate(my_tasks):
        if task.id == id:
            my_tasks.pop(i)
            return 1
    return None
 
@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")

@app.get("/tasks")
def read_tasks():
    return get_tasks()

@app.post("/tasks")
def create_task(task: Task):
    return create_tasks(task)

@app.get("/tasks/{id}")
def read_task(id: int):
    return get_task_by_id(id)

@app.put("/tasks/{id}")
def update_task(id: int, task: Task):
    return update_tasks(id, task)

@app.delete("/tasks/{id}")
def delete_task(id: int):
    return delete_tasks(id)


