
# Employee Management System

This is a Python-based Employee Management System that allows users to manage employee details such as adding, modifying, deleting, and viewing employee information. The system leverages core Object-Oriented Programming (OOP) concepts to ensure that the application is modular, scalable, and easily maintainable.

## Features
- Add new employees with detailed attributes like ID, Name, Age, Department, Salary, Email, Phone, and Address.
- Modify employee details while showing the existing data.
- Delete employee records individually or remove all records at once.
- Display employee data in a tabular format.
- Search employees by their ID or name.
- Robust error handling and input validation.

## Installation Instructions

To set up the Employee Management System on your local machine, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/YourUsername/Employee-Management-System.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Employee-Management-System
    ```

3. Make sure you have Python installed (preferably version 3.x).

4. Run the program:
    ```bash
    python employee_management_system.py
    ```

Note: No additional dependencies are required as this is a basic Python project using standard libraries.

## Usage

Once you run the program, a menu with the following options will appear:

1. **Add Employee**: Enter details of a new employee.
2. **Delete Employee**: Delete an existing employee using their ID.
3. **Modify Employee**: Modify an employee’s details (name, age, department, etc.).
4. **Display All Employees**: View all employee records in a table format.
5. **Find Employee by ID**: Search for an employee using their ID.
6. **Find Employee by Name**: Search for an employee using their name.
7. **Delete All Employees**: Delete all employee records from the system.
8. **Exit**: Exit the program.

Follow the on-screen instructions to interact with the system.

## Technologies Used

- Python 3.x
- Object-Oriented Programming (OOP)
- No external libraries were used (just Python’s standard library)

## OOP Concepts Implemented

This project incorporates the following core OOP concepts:

- **Classes & Objects**: The `Employee` class defines employee data, while the `EmployeeManager` class manages all employee-related operations.
- **Encapsulation**: Data within the `Employee` class is encapsulated, and access is provided through methods.
- **Abstraction**: Complex operations like adding and deleting employees are abstracted behind simple method calls.
- **Polymorphism**: Methods like `display_all_employees` and `modify_employee` are implemented with flexibility, allowing them to handle different inputs dynamically.
 

## Acknowledgments

- Special thanks to **KV Srinivas** for his excellent training and guidance.
- Huge thanks to **Sunil Reddy** for coordinating and supporting the project.
- Thanks to all contributors and collaborators who made this project possible.
