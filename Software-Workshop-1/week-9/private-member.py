class Employee:
# constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary # Double underscores __ for a private member

    def show(self):
        print(self.name, self.__salary)


# creating object of a class
emp = Employee('Todd', 50000)
emp.show()

# accessing private data members using name mangling
print('Salary:', emp._Employee__salary)

# accessing private data members
print('Salary:', emp.__salary)