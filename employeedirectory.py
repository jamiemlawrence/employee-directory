employee_list = []

# Employee class to store info
class Employee:
    def __init__(self, name, id, position, salary):
        self.name = name
        self.id = id
        self.position = position
        self.salary = salary
    def display_info(self):
        return {'name': self.name, 'id': self.id, 'position': self.position, 'salary': self.salary}

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

# Checks for empty employee list and returns full directory       
def employee_directory():
    if not employee_list:
        print("There are currently no employees in the directory.")
        return
    print("\nEmployee Directory:")
    for employee in employee_list:
        info = employee.display_info()
        print(f"\nEmployee ID: {info['id']}")
        print(f"Name: {info['name']}")
        print(f"Position: {info['position']}")
        print(f"Salary: ${info['salary']}")

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
        print("3. Find Employee")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            employee_directory()
        elif choice == '2':
            add_employee()
        elif choice == '3':
            employee_lookup()
        elif choice == '4':
            print("Exiting payroll system.")
            break
        else:
            print("Invalid choice. Please select one of the optoins")
    
menu()
