from db_connector import connect

cursor, mydb = connect()


def setup():
    cursor.execute('create database if not exists hrapp')
    cursor.execute('use hrapp')
    cursor.execute(
        'create table if not exists employees(id int auto_increment,name text,position text, department_id int, salary int, primary key(id))')
    cursor.execute(
        'create table if not exists departments(id int auto_increment,name text, primary key(id))')


setup()


def addNewDepartment():

    department_name = input("Please enter the department name : ")

    cursor.execute("insert into departments (name) values (%s)",
                   [department_name])
    mydb.commit()


def displayAllDepartments():
    cursor.execute("Select * from departments")
    for department in cursor.fetchall():
        print(f'[{department[0]}] - {department[1]} Department')


def addNewEmployee():
    name = input("Please enter the employee name :")
    position = input("Please enter the job position : ")
    salary = input("Please enter the salary : ")
    displayAllDepartments()
    department_id = input("Please enter department id : ")
    cursor.execute(
        "insert into employees set name = %s, position = %s, salary = %s, department_id = %s",
        [name, position, salary, department_id])
    mydb.commit()
    displayAllEmployees()


def displayAllEmployees():
    cursor.execute("Select * from employees")
    for employee in cursor.fetchall():
        print(f'[{employee[0]}] - {employee[1]} - Position - {employee[2]}'
              f' - Department {employee[3]}'
              f' - Salary {employee[4]} Ks')


def getEmployeeById(id):
    cursor.execute("select * from employees where id = %s", [id])
    employee = cursor.fetchone()
    return employee


def increaseSalary():
    print("Preparing to increase salary")
    displayAllEmployees()
    employee_id = input("Please select the employee : ")
    employee = getEmployeeById(employee_id)
    user_choise = input(
        f"Are you sure you want to raise {employee[1]}'s salary? : y/n \n")
    if(user_choise == 'y'):
        increase_amount = int(input("How much do you want to increase : "))
        new_salary = increase_amount + int(employee[4])
        cursor.execute("Update employees set salary = %s where id = %s",
                       [new_salary, employee_id])
        mydb.commit()
        displayAllEmployees()


def displayMenu():
    try:
        selected_option = input(
            f'Please select the action you want to do.\n'
            f'[1] Add New Employee\n'
            f'[2] Add New Department\n'
            f'[3] View All Employee\n'
            f'[4] View All Departments\n'
            f'[5] Increase Salary\n'
        )

        if(selected_option == '1'):
            addNewEmployee()
        elif(selected_option == '2'):
            addNewDepartment()
        elif(selected_option == '3'):
            displayAllEmployees()
        elif(selected_option == '4'):
            displayAllDepartments()
        elif(selected_option == '5'):
            increaseSalary()
        user_choice = input("Do you want to go back to menu? : y/n \n")
        if(user_choice == 'y'):
            displayMenu()
        else:
            print("Bye Bye")
    except KeyboardInterrupt:
        print("Bye bye")


displayMenu()
