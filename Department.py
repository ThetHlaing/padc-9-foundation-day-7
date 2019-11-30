from Database import Database


class Department:
    id = None
    name = None

    def __init__(self,tuple_data = None):
        if(tuple_data):
            self.id = tuple_data[0]
            self.name = tuple_data[1]
        #print("Department class is initialized")

    def save(self):
        Database._cursor.execute(
            "insert into departments (name) values (%s)", [self.name])
        Database._db.commit()
        self.id = Database._cursor.lastrowid
        self.display()

    def display(self):
        print(f'[{self.id}] - {self.name} Department')

    @staticmethod
    def find(id):
        Database._cursor.execute("Select * from departments where id = %s",[id])
        result = Database._cursor.fetchone()
        return Department(result)
    
    @staticmethod
    def get():
        Database._cursor.execute("Select * from departments")
        department_list = []
        for departmentTuple in Database._cursor.fetchall():
            department = Department(departmentTuple)
            department_list.append(department)
        return department_list