class Student:
    def __init__(self, name, rollno) -> None:
        self.name = name
        self.rollno = rollno

    def show(self):
        print(self.name, self.rollno)


object1 = Student("Ali", 111)

object1.show()
print(object1.name, object1.rollno)