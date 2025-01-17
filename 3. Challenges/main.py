from student import Student
from merit import MeritChecker

name = input("Enter the name of the Student: ")
roll_no = input("Enter the roll number of the Student: ")
num_subjects = int(input("Enter the number of Subjects: "))

student = Student(name, roll_no)
student.getMarks(num_subjects)

MeritChecker.check_merit(student)