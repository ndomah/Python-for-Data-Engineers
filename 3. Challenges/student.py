class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = []
        
    def getMarks(self, num_subjects):
        for i in range(1, num_subjects + 1):
            mark = int(input(f"Enter marks{i}: "))
            self.marks.append(mark)