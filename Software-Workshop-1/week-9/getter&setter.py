class Employee:
# constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary # Double underscores __ for a private member

    def show(self):
        print(self.name, self.__salary)

    # To ensure data encapsulation
    def get_salary(self):
        return self.__salary
    
    # To ensure data encapsulation
    def set_salary(self, salary):
        self.__salary = salary

# creating object of a class
emp = Employee('Todd', 50000)
emp.show()

# accessing private data members
print('Salary:', emp.get_salary())
emp.set_salary(60000)
print('Salary:', emp.get_salary())
