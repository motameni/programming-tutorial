# Define a class that represent the student concept. Each student should
# have id_number, name, age, major, and marks attributes. Also, it should
# have add_mark(self, mark) to add a new mark and get_average(self) method
# to calculate and return the average of the marks.

class Student:
    marks = []
    marks_sum = 0
    marks_number = 0

    def __init__(self, id_number, name, age, major):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.major = major

    def add_mark(self, mark):
        self.marks.append(mark)
        self.marks_sum += mark
        self.marks_number += 1

    def add_marks(self, marks):
        for mark in marks:
            self.add_mark(mark)

    def get_average(self):
        return self.marks_sum / self.marks_number

    def print_average(self):
        print("%.2f" % self.get_average())


ali = Student("123", "Ali Motameni", 31, "Computer Engineering")
ali.add_marks([19, 20, 19, 18, 17])
ali.print_average()

ali.add_mark(19)
ali.print_average()
