class Student:
    def __init__(self, student_id : int, name : str, course : str):
        #Validation
        assert student_id > 0, "Student ID must be a positive number."

        #Instance variables
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if student.student_id in self.students:
            print(f"Student with ID {student.student_id} already exists.")
        else:
            self.students[student.student_id] = student
            print(f"Added student: {student.name}")

    def remove_student(self, student_id):
        if student_id in self.students:
            removed_student = self.students.pop(student_id)
            print(f"Removed student: {removed_student.name}")
        else:
            print(f"No student found with ID {student_id}.")

    def search_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print("Student found:", student)
        else:
            print(f"No student found with ID {student_id}.")

try:
    # Example usage:
    sms = StudentManagementSystem()

    # Adding students
    s1 = Student(101, "Amal", "Computer Science")
    s2 = Student(102, "Rida", "Data Science")

    sms.add_student(s1)
    sms.add_student(s2)

    # Searching a student
    sms.search_student(101)

    # Removing a student
    sms.remove_student(102)

    # Trying to remove again
    sms.remove_student(102)
except AssertionError as e:
    print(f"Error message : {e}")
