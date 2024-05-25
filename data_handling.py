import sqlite3

class Database:
    def __init__(self, con, cur) -> None:
        self.con = con
        self.cur = cur

        self.todo_list = []

    @property
    def todo_list(self):
        return self._todo_list

    @todo_list.setter
    def todo_list(self, value):
        self.cur.execute("""SELECT * from ToDo""")
        self._todo_list = self.cur.fetchall()
    
    @classmethod
    def get(cls):
        con = sqlite3.connect("list.db")
        cur = con.cursor()
        return cls(con, cur)

    def close(self):
        self.con.close()

    def createTable(self):
        self.cur.execute("""CREATE TABLE ToDo (
                    id integer,
                    title text,
                    content text,
                    status integer
                    )""")
        self.con.commit()

    def addToDo(self, title, content):
        id = 1
        while True:
            if id in [i[0] for i in self.todo_list]:
                id+=1
            else:
                break
        
        self.cur.execute(f"""INSERT INTO ToDo VALUES (
                    {id},
                    "{title}", 
                    "{content}",
                    False
                    )""")
        self.con.commit()

    def deleteToDo(self, id):
        self.cur.execute(f"""DELETE from ToDo where id = {id}""")
        self.con.commit()

    def modifyToDo(self, id, title, content,status):
        self.cur.execute(f"""UPDATE ToDo
                    SET title = "{title}",
                    content ="{content}",
                    status = {status}
                    WHERE id = {id}""")
        self.con.commit()

def retrieveToDo(cur):
    cur.execute("""SELECT * from ToDo""")
    return cur.fetchall()

#createTable(cur)
#addToDo(cur, "NNN", "DO NOT NUT", "12.1.2024")
#deleteToDo(cur, 2)
#modifyToDo(cur, 1, "papa", "pig")

#print(retrieveToDo(cur))