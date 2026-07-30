#4.student grade management

class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
        self.__marks = []

    def add_marks(self):
        for i in range(3):
            mark = int(input(f"Enter Marks for Subject {i+1}: "))
            self.__marks.append(mark)

    def get_marks(self):
        return self.__marks


class GradeCalculator(Student):
    def calculate(self):
        marks = self.get_marks()
        total = sum(marks)
        average = total / len(marks)

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        print("\n------ Student Report ------")
        print("Roll No :", self.roll)
        print("Name    :", self.name)
        print("Marks   :", marks)
        print("Total   :", total)
        print("Average :", average)
        print("Grade   :", grade)


student = GradeCalculator(104, "Ananya")
student.add_marks()
student.calculate()