class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'ОШИБКА!'

    def average_grade(self):
        sum_grades = 0
        len_grades = 0
        for course in self.grades.values():
            sum_grades += sum(course)
            len_grades += len(course)
        avg_grade = round(sum_grades / len_grades, 1)
        return avg_grade

    def __str__(self):
        return f' Имя студента: {self.name}\n Фамилия студента: {self.surname}\n Средняя оценка за ДЗ: {self.average_grade()}\n Курсы в процессе: {",".join(self.courses_in_progress)}\n Завершенные курсы:{", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нельзя сравнить...")
            return
        return self.average_grade() < other.average_grade() 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def average_grade(self):
        sum_grades = 0
        len_grades = 0
        for course in self.grades.values():
            sum_grades += sum(course)
            len_grades += len(course)
        avg_grades = round(sum_grades / len_grades, 1)
        return avg_grades

    def __str__(self):
        return f' Имя лектора: {self.name}\n Фамилия лектора: {self.surname}\n Средняя оценка за лекции: {self.average_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нельзя сравнить...")
            return
        return self.average_grade() < other.average_grade()

class Reviewer(Mentor):
    def __int__(self, name, surname):
        super.__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'ОШИБКА!'
    
    def __str__(self):
        return f' Имя проверяющего: {self.name}\n Фамилия проверяющего: {self.surname}'
 
# Студенты N1-N2

first_student = Student('Вася', 'Пупкин', 'муж')
first_student.courses_in_progress += ['HTML, CSS, JS']
first_student.finished_courses += ['Python']

second_student = Student('Варвара', 'Краса', 'жен')
second_student.courses_in_progress += ['HTML, CSS, JS']
second_student.finished_courses += ['Python']

# Лекторы N1-N2

first_lecturer = Lecturer('Наталья', 'Орейро')
first_lecturer.courses_attached += ['HTML, CSS, JS']

second_lecturer = Lecturer('Дейзи', 'Джонсон')
second_lecturer.courses_attached += ['HTML, CSS, JS']

# Проверяющие N1-N2

first_reviewer = Reviewer('Главный', 'Ревизор')
first_reviewer.courses_attached += ['HTML, CSS, JS']

second_reviewer = Reviewer('Помощник', 'Ревизора')
second_reviewer.courses_attached += ['HTML, CSS, JS']

# Оценки Студентам N1-N2 за ДЗ

first_reviewer.rate_hw(first_student, 'HTML, CSS, JS', 10)
first_reviewer.rate_hw(first_student, 'HTML, CSS, JS', 7)
first_reviewer.rate_hw(first_student, 'HTML, CSS, JS', 5)

second_reviewer.rate_hw(second_student, 'HTML, CSS, JS', 4)
second_reviewer.rate_hw(second_student, 'HTML, CSS, JS', 6)
second_reviewer.rate_hw(second_student, 'HTML, CSS, JS', 2)

# Оценки Лекторовым за лекцию

first_student.rate_lecture(first_lecturer, 'HTML, CSS, JS', 6)
first_student.rate_lecture(first_lecturer, 'HTML, CSS, JS', 7)
first_student.rate_lecture(first_lecturer, 'HTML, CSS, JS', 10)

second_student.rate_lecture(second_lecturer, 'HTML, CSS, JS', 10)
second_student.rate_lecture(second_lecturer, 'HTML, CSS, JS', 9)
second_student.rate_lecture(second_lecturer, 'HTML, CSS, JS', 7)

print('\nСтуденты:')
print('=' * 10)
print(first_student)
print('-' * 10)
print(second_student)

print('\nЛекторы:')
print('=' * 10)
print(first_lecturer)
print('-' * 10)
print(second_lecturer)

print('\nПроверяющие:')
print('=' * 10)
print(first_reviewer)
print('-' * 10)
print(second_reviewer)
print('=' * 10)