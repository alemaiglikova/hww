import json
import requests

class Todo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

    def json(self):
        dict={"userid":self.userId, "id":self.id, "title":self.title, "completed": self.completed}
        with open(f"todo_{self.id}.json", "w") as json_file:
            json.dump(dict, json_file)

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = response.json()
for todo in todos:
    todo_object = Todo(todo["userId"], todo["id"], todo["title"], todo["completed"])
    todo_object.save_to_json()