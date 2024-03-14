class Student:
    """Represents a student."""
    def __init__(self, name, number) -> None:
        "Cibstryctir creates a Student with the given name and number of scores and sets all scores to 0"
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        "Return the student's name"
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1"""
        return self.scores[i - 1]
    
    def getAverage(self):
        """Return the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Return the average score."""
        return max(self.scores)
    
    def __str__(self) -> str:
        """Return the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + \
        " ".join(map(str, self.scores))
    
    # Q1.b.
    def __lt__(self, other):
        result = []
        for i in range(len(self.scores)):
            result.append(self.scores[i] < other.scores[i])
        return result
        
    def __eq__(self, other):
        result = []
        for i in range(len(self.scores)):
            result.append(self.scores[i] == other.scores[i])
        return result
    
    def __ge__(self, other):
        result = []
        for i in range(len(self.scores)):
            result.append(self.scores[i] >= other.scores[i])
        return result


def main():
    # Q1.b.
    # Creating student objects
    student1 = Student("Alice", 2)
    student2 = Student("Bob", 2)

    print()
    student1.setScore(1, 90)
    student1.setScore(2, 94)
    print(f"{student1.getName()}'s score 1 is :" ,student1.getScore(1))
    print("Avreage score: ", student1.getAverage())
    print("Highest score: ",student1.getHighScore())

    student2.setScore(1, 85)
    student2.setScore(2, 95)
    print(f"{student2.getName()}'s score 1 is :" ,student2.getScore(1))
    print("Avreage score: ", student2.getAverage())
    print("Highest score: ",student2.getHighScore())

    # Testing comparison operators
    print(f"Are {student1.name} and {student2.name} equal?\n{student1.__eq__(student2)}\n")
    print(f"Is {student1.name} less than {student2.name}?\n{student1.__lt__(student2)}\n")
    print(f"Is {student1.name} greater than or equal to {student2.name}?\n{student1.__ge__(student2)}\n")


if __name__ == "__main__":
    main()