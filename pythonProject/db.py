import sqlite3

class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
        id Integer primary key,
        name text,
        age text,
        doj text,
        email text,
        gender text,
        contact text,
        address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # insert Function
    def insert(self, name, age, doj, email, gender, contact, address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
                         (name, age, doj, email, gender, contact, address))
        self.con.commit()

    # Fetch All Data from db
    def fetch(self):
        self.cur.execute("Select * from employees")
        rows=self.cur.fetchall()
        #print(rows)
        return rows

    # Delete a Record in db
    def remove(self, id):
        self.cur.execute("Delete from employees where id=?", (id,))
        self.con.commit()

    # Update a Record in db
    def update(self, id, name, age, doj, email, gender, contact, address):
        self.cur.execute("update employees set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?",
                         (name, age, doj, email, gender, contact, address,id))
        self.con.commit()

