employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
}

def main_menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using EMS. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

def add_employee():
    print("\n--- Add New Employee ---")

    while True:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("This ID already exists! Try another.")
        else:
            break

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    salary = int(input("Enter Salary: "))

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print("Employee added successfully!")

def view_employees():
    print("\n--- Employee List ---")

    if not employees:
        print("No employees available.")
        return

    print("{:<10} {:<15} {:<10} {:<15} {:<10}".format(
        "Emp ID", "Name", "Age", "Department", "Salary"))

    for emp_id, details in employees.items():
        print("{:<10} {:<15} {:<10} {:<15} {:<10}".format(
            emp_id,
            details['name'],
            details['age'],
            details['department'],
            details['salary']
        ))

def search_employee():
    print("\n--- Search Employee ---")

    emp_id = int(input("Enter Employee ID to search: "))

    if emp_id in employees:
        details = employees[emp_id]
        print("\nEmployee Found:")
        print("Name:", details['name'])
        print("Age:", details['age'])
        print("Department:", details['department'])
        print("Salary:", details['salary'])
    else:
        print("Employee not found.")
main_menu()


