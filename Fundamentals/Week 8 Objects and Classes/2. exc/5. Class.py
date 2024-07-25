
class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.grades)
        return float(f"{average_grade:.2f}")
        # ако не го задам като с float ще го return-e като string и ще даде грешка в Judge

    def __repr__(self):
        students = ", ".join(self.students)  # за да отпечатам листа ", "
        if not self.students:  # проверка дали листа е празен
            ave_grade = "2.00"
        else:
            ave_grade = self.get_average_grade()  # мога и с self.get_average_grade() да отпечатам (ave_grade)
        return f"The students in {self.name}: {students}. Average grade: {ave_grade}"  # така всички са string


a_class = Class("11B")
print(a_class)  # този принт ако листитв са празни ще чупи кода без горния if
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
