from Department import Department
from Employee import Employee


def addNewDepartment():

    deparment = Department()
    deparment.name = input("Please enter the department name : ")
    deparment.save()


def displayAllDepartments():
    department_list = Department.get()
    # cursor.execute("Select * from departments")
    for department in department_list:
        department.display()


def addNewEmployee():
    employee = Employee()
    employee.name = input("Please enter the employee name :")
    employee.position = input("Please enter the job position : ")
    employee.salary = input("Please enter the salary : ")
    displayAllDepartments()
    employee.department_id = input("Please enter department id : ")
    employee.save()


def displayAllEmployees():
    employees = Employee.get()
    for employee in employees:
        employee.display()

def increaseSalary():
    print("Preparing to increase salary")
    displayAllEmployees()
    employee_id = input("Please select the employee : ")
    employee = Employee.find(employee_id)
    user_choise = input(
        f"Are you sure you want to raise {employee.name}'s salary? : y/n \n")
    if(user_choise == 'y'):
        increase_amount = int(input("How much do you want to increase : "))
        # employee.name = "This is going to be update"
        employee.salary = increase_amount + int(employee.salary)
        employee.update()
        


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
