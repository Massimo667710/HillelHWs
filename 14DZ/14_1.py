class GroupFullError(Exception):
    def __init__(self, message="Group cannot have more than 10 students."):
        self.message = message
        super().__init__(self.message)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.gender}, {self.age} years old)\n'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        self.record_book = record_book
        super().__init__(gender, age, first_name, last_name)

    def __str__(self):
        resp = super().__str__()
        return f'Student {self.record_book}: ' + resp


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupFullError(f"Cannot add {student.first_name} {student.last_name}: Group {self.number} is full.")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student)
        return f'Number: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 22, 'Sarah', 'Connor', 'AN146')
st4 = Student('Male', 23, 'John', 'Doe', 'AN147')
st5 = Student('Male', 24, 'Michael', 'Smith', 'AN148')

gr = Group('PD1')
students = [st1, st2, st3, st4, st5]

for student in students:
    try:
        gr.add_student(student)
        print(f"Added {student.first_name} {student.last_name} to group {gr.number}.")
    except GroupFullError as e:
        print(e)

print(gr)
