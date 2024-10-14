from tabulate import tabulate

# Employee class to store info
class Employee:
    def __init__(self, name, id, position, salary):
        self.name = name
        self.id = id
        self.position = position
        self.salary = salary
    def display_info(self):
        return {'name': self.name, 'id': self.id, 'position': self.position, 'salary': self.salary}

# Initial empty employee list
employee_list = []

# Prompts user to enter employee info and adds to directory
def add_employee():
    print("Adding employee...")
    name = input("Enter employee name: ")
    id = input("Enter employee ID: ")
    position = input("Enter employee position: ")
    while True:
        try:
            salary = float(input("Enter salary: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for salary.")
    employee = Employee(name, id, position, salary)
    employee_list.append(employee)
    print("Employee profile created successfully")

# Checks for employee in list and returns info and removes employee
def remove_employee():
    if not employee_list:
        print("No employee profiles found. Please add an employee first.")
        return
    employee_id = input("Enter the employee ID to remove: ")
    for employee in employee_list:
        if employee.id == employee_id:
            employee_list.remove(employee)
            print(f"Employee {employee.name} (ID: {employee.id}) has been removed.")
            return
    print("Employee not found.")

# Checks for empty employee list and returns full directory using Tabulate      
def employee_directory():
    if not employee_list:
        print("There are currently no employees in the directory.")
        return
    headers = ["Name", "ID", "Position", "Salary", "Department"]
    table = [emp.display_info().values() for emp in employee_list]
    print(tabulate(table, headers, tablefmt="grid"))

# Checks empty employee list, then searches for employee by ID and returns if found 
def employee_lookup():
    if not employee_list:
        print("No employee profiles found. Please add an employee first")
        return
    employee_id = input("Enter employee ID: ")
    found_employee = None
    for employee in employee_list:
        if employee.id == employee_id:
            found_employee = employee
            break
    if found_employee:
        info = found_employee.display_info()
        print("\nEmployee Details:")
        for key, value in info.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Employee not found.")

# Navigation menu
def menu():
    while True:
        print("\n*** Payroll System Menu ***")
        print("1. View Employee Directory")
        print("2. Add Employee")
        print("3. Remove Employee")
        print("4. Find Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            employee_directory()
        elif choice == '2':
            add_employee()
        elif choice == '3':
            remove_employee()
        elif choice == '4':
            employee_lookup()
        elif choice == '5':
            print("Exiting payroll system.")
            break
        else:
            print("Invalid choice. Please select one of the optoins")
    
menu()
