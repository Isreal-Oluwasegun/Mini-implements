# Todo App
# Add, Delete, Show and Update task
import sqlite3


class Todo:
    
    def __init__(self):
        self.conn = sqlite3.Connection('Todo')
        
        self.c = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            priority INTEGER NOT NULL
        );
                       """)
        
    def find_task(self, name):
        for row in self.c.execute("SELECT * FROM tasks"):
            if row[1] == name: 
                return row
        return None
        
    def add_tasks(self):
        name = input("Enter the task name: ")
        priority = input("Set priority level (1-3) ")
        if len(name) == 0 or int(priority) < 1:
            return
        
        check = self.find_task(name)
        if check is not None:
            print("Task already exist\n")
            return
        self.c.execute("INSERT INTO tasks(name, priority) VALUES(?,?)", (name, priority))
        self.conn.commit()
        
    def show_tasks(self):
        for rows in self.c.execute("SELECT * FROM tasks"):
            print(rows)
            
    def is_empty(self):
        for rows in self.c.execute("SELECT * FROM tasks"):
            if len(rows) != 0:
                return rows
        return None
        
    def delete_task(self):
        if self.is_empty() is None:
            print("\nYou have no more item in Todo\n")
            return 
        self.delete_val = int(input("Delete task number: "))
        self.c.execute("DELETE FROM tasks WHERE id =?",(self.delete_val,))
        self.conn.commit()
            

        
app = Todo()
while (user := input("Welcome to Todo\n\ta to add task\n\ts to show all tasks\n\td to delete task\n Enter here: ")) != 'q':
    if user == 'a':
        app.add_tasks()
    elif user == 's':
        app.show_tasks()
    else:
        app.delete_task()
        break

        
        
        
        