def get_student_grade(student_name, grades_dict):
    try:
        grade = grades_dict[student_name]
        return f"{student_name}'s grade is {grade}"
    except KeyError:
        return f"Student '{student_name}' not found in the dictionary."

# Example dictionary of student names and grades
student_grades = {
    "Hongbo": "Distinction",
    "Hamaz": "Merit",
    "Bruce": "Distinction",
    "Wayne": "Distinction",
    "Fayrouz": "Merit"
}

while True:
    student_name = input("Enter you name to check your grade, 'q' for exit: ")
    if student_name == 'q':
        break
    result = get_student_grade(student_name, student_grades)
    print(result)

