class Employee:
    """Class to represent an employee."""

    def __init__(self, emp_id, name, age, department, salary, email, phone, address):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
        self.email = email
        self.phone = phone
        self.address = address

    def to_list(self):
        """Convert employee details to a list for table display."""
        return [
            str(self.emp_id), self.name, str(self.age), self.department,
            f"{self.salary:.2f}", self.email, self.phone, self.address
        ]


class EmployeeManager:
    """Class to manage employee details."""

    def __init__(self):
        self.employees = {}

    def add_employee(self, employee):
        """Add an employee to the system."""
        if employee.emp_id in self.employees:
            print(f"Employee with ID {employee.emp_id} already exists.")
        else:
            self.employees[employee.emp_id] = employee
            print(f"Employee {employee.name} added successfully.")

    def delete_employee(self, emp_id):
        """Delete an employee from the system."""
        if emp_id in self.employees:
            del self.employees[emp_id]
            print(f"Employee with ID {emp_id} deleted successfully.")
        else:
            print(f"Employee with ID {emp_id} does not exist.")

    def delete_all_employees(self):
        """Delete all employees from the system."""
        if self.employees:
            self.employees.clear()
            print("All employee details have been deleted.")
        else:
            print("No employees to delete.")

    def modify_employee(self, emp_id):
        """Modify employee details."""
        if emp_id in self.employees:
            employee = self.employees[emp_id]
            print(f"Modifying details for Employee ID {emp_id}.")
            print("Press Enter to keep the existing value.")

            name = input(f"Name [{employee.name}]: ") or employee.name
            age = input(f"Age [{employee.age}]: ")
            age = int(age) if age else employee.age
            department = input(f"Department [{employee.department}]: ") or employee.department
            salary = input(f"Salary [{employee.salary}]: ")
            salary = float(salary) if salary else employee.salary
            email = input(f"Email [{employee.email}]: ") or employee.email
            phone = input(f"Phone [{employee.phone}]: ") or employee.phone
            address = input(f"Address [{employee.address}]: ") or employee.address

            employee.name = name
            employee.age = age
            employee.department = department
            employee.salary = salary
            employee.email = email
            employee.phone = phone
            employee.address = address

            print(f"Employee ID {emp_id} details updated successfully.")
        else:
            print(f"Employee with ID {emp_id} does not exist.")

    def display_all_employees(self):
        """Display all employees' details in a tabular format."""
        if self.employees:
            headers = ["ID", "Name", "Age", "Department", "Salary", "Email", "Phone", "Address"]
            rows = [employee.to_list() for employee in self.employees.values()]
            self.print_table(headers, rows)
        else:
            print("No employees to display.")

    def find_employee_by_id(self, emp_id):
        """Find and display an employee by ID."""
        if emp_id in self.employees:
            headers = ["ID", "Name", "Age", "Department", "Salary", "Email", "Phone", "Address"]
            rows = [self.employees[emp_id].to_list()]
            self.print_table(headers, rows)
        else:
            print(f"Employee with ID {emp_id} does not exist.")

    def find_employee_by_name(self, name):
        """Find and display employees by name."""
        found = False
        headers = ["ID", "Name", "Age", "Department", "Salary", "Email", "Phone", "Address"]
        rows = []
        for employee in self.employees.values():
            if employee.name.lower() == name.lower():
                rows.append(employee.to_list())
                found = True
        if found:
            self.print_table(headers, rows)
        else:
            print(f"No employees found with the name {name}.")

    @staticmethod
    def print_table(headers, rows):
        """Print data in a tabular format."""
        # Calculate column widths
        col_widths = [max(len(str(row[i])) for row in rows + [headers]) for i in range(len(headers))]

        # Print header
        header_row = " | ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
        print("-" * len(header_row))
        print(header_row)
        print("-" * len(header_row))

        # Print rows
        for row in rows:
            print(" | ".join(f"{row[i]:<{col_widths[i]}}" for i in range(len(row))))
        print("-" * len(header_row))


def main():
    manager = EmployeeManager()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Modify Employee")
        print("4. Display All Employees")
        print("5. Find Employee by ID")
        print("6. Find Employee by Name")
        print("7. Delete All Employees")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Add employee
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            email = input("Enter Email: ")
            phone = input("Enter Phone: ")
            address = input("Enter Address: ")
            employee = Employee(emp_id, name, age, department, salary, email, phone, address)
            manager.add_employee(employee)

        elif choice == '2':
            # Delete employee
            emp_id = int(input("Enter Employee ID to delete: "))
            manager.delete_employee(emp_id)

        elif choice == '3':
            # Modify employee
            emp_id = int(input("Enter Employee ID to modify: "))
            manager.modify_employee(emp_id)

        elif choice == '4':
            # Display all employees
            manager.display_all_employees()

        elif choice == '5':
            # Find employee by ID
            emp_id = int(input("Enter Employee ID to find: "))
            manager.find_employee_by_id(emp_id)

        elif choice == '6':
            # Find employee by name
            name = input("Enter Employee Name to find: ")
            manager.find_employee_by_name(name)

        elif choice == '7':
            # Delete all employees
            manager.delete_all_employees()

        elif choice == '8':
            # Exit
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
