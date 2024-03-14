class HRManager:
    annual_salary = 900000
    # Class attributes
    def __init__(self, name, age, department, phone):
        self.name = name
        self.age = age
        self.department = department
        self.phone = phone


class Employee:
    # Class attributes
    annual_salary = 660000

    def __init__(self, name, age, address, phone, department):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.department = department

# Program ==================================================================

# Function that prints the monthly salary of each employee
# and the total payroll expense for the company
def process_payroll(employees):

    total_payroll_expense = 0
    print("\n========= Welcome to the HR Payroll System =========\n")

    # Iterate over the list of instances to calculate
    # and display the monthly salary for each employee,
    # and add the total payroll expense
    for emp in employees:
        monthly_salary = emp.annual_salary / 12
        print(f"{emp.name.capitalize()}'s monthly salary is: ${monthly_salary:.2f}")
        total_payroll_expense += monthly_salary

    # Print the total payroll expense for the month
    print(f"\nThe total payroll expense for the month is: ${total_payroll_expense:.2f}")

# Instances (employees)
jack = HRManager("jack", 50, "Human Resources", "555-321-4567")
isabel = Employee("isabel", 28, "123 Maple St", "555-654-1234", "Marketing")

# List of employee instances
employees = [jack, isabel]

# Call the function, passing in the list of employee instances
process_payroll(employees)