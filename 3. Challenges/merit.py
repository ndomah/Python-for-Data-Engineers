from student import Student 

class MeritChecker:
    
    @staticmethod
    def check_merit(student):
        if not student.marks:
            print("Marks are not entered.")
            return
        
        avg_marks = sum(student.marks) / len(student.marks)
        if avg_marks > 90:
            print(f"{student.name} with Roll No: {student.roll_no}, is eligible for merit.")
        else:
            print(f"{student.name} with Roll No: {student.roll_no}, is not eligible.")