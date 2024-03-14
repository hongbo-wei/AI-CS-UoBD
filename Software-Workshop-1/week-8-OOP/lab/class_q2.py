import random


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
    
    def __lt__(self, other):
        """Returns self < other, with respect
        to names."""
        return self.name < other.name

    def __ge__(self, other):
        """Returns self >= other, with respect
        to names."""
        return self.name >= other.name

    def __eq__(self, other):
        """Tests for equality."""
        return self.name == other.name



def main():
    # Q2
    number_of_score = 4
    students = [Student("Alice", number_of_score),
                Student("Bob", number_of_score),
                Student("Charlie", number_of_score),
                Student("David", number_of_score)]
    
    for i in range(len(students)):
        for j in range(4):
            students[i].scores[j] = random.randint(1,100)

    # Shuffling the list using random.shuffle()
    random.shuffle(students)
    print(f"List after shuffling:")
    for student in students:
        print(student)
    print()

    students.sort()
    print(f"List after sorting:")
    for student in students:
        print(student)


if __name__ == "__main__":
    main()