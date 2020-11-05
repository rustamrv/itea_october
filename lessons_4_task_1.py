from abc import ABC, abstractmethod
from datetime import date


class Person(ABC):
    list_of_person = []

    def __init__(self, first_name, surname, birthday):
        self._first_name = first_name
        self._surname = surname
        self.birthday = birthday
        self.__class__.list_of_person.append(self)

    @abstractmethod
    def info(self):
        print(f'Hi, my fullname {self.full_name}, '
              f'my birthday {self.birthday}')

    @property
    def first_name(self):
        return self._first_name

    @property
    def surname(self):
        return self._surname

    @property
    def full_name(self):
        return f'{self.first_name} {self.surname}'

    @property
    def age(self):
        today = date.today()
        return today.year - self.birthday.year - \
               ((today.month, today.day) < (self.birthday.month, self.birthday.day))


class Matriculant(Person):

    def __init__(self, first_name, surname, birthday, faculty):
        super(Matriculant, self).__init__(first_name, surname, birthday)
        self.faculty = faculty

    def info(self):
        print(f'Hi, my name is {self.full_name} '
              f'and I am an matriculant, '
              f'my birthday {self.birthday}, '
              f'faculty of {self.faculty},'
              f'age now {self.age}')


class Student(Matriculant):

    def __init__(self, first_name, surname, birthday, faculty, course):
        super(Student, self).__init__(first_name, surname, birthday,
                                      faculty)
        self.course = course

    def info(self):
        print(f'Hi, my name is {self.full_name} '
              f'and I am an student, '
              f'faculty of {self.faculty}, '
              f'course {self.course},'
              f'age now {self.age}')


class Teacher(Person):

    def __init__(self, first_name, surname, birthday, faculty, position, experience):
        super(Teacher, self).__init__(first_name, surname, birthday)
        self.faculty = faculty
        self.position = position
        self.experience = experience

    def info(self):
        print(f'Hi, my name is {self.full_name} '
              f'and I am an teacher, '
              f'faculty of {self.faculty}, '
              f'position {self.position}, '
              f'experience {self.experience}, '
              f'age now {self.age}')


if __name__ == "__main__":
    person1 = Matriculant('Ivanov', 'Ivan', date(1993, 5, 7), "FIOT")
    person1.info()
    student = Student('Petrov', 'Ivan', date(1969, 8, 10), "Mathematics", 5)
    student.info()
    teacher = Teacher('Ivanov', 'Danil', date(1980, 8, 10), "Mathematics", "Programmer", 5)
    teacher.info()

    array = [i.full_name for i in Person.list_of_person if 40 <= i.age <= 51]
    print(array)
