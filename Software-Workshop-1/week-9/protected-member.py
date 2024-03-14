class Employee:
# constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self._salary = salary # Single _ for a protected member

    def show(self):
        print(self.name, self._salary)

    # To ensure data encapsulation
    def get_salary(self):
        return self._salary
    

# creating object of a class
emp = Employee('Todd', 50000)
emp.show()

# accessing protect data members
print('Salary:', emp._salary) # Can be accessed but it is a bad practice

print('Salary:', emp.get_salary()) # A good practice