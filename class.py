class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print('Недопустимый возраст')

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f'Name: {self.__name}, Age: {self.__age}')


class Employee(Person):

    def __init__(self, name, age, company):
        Person.__init__(self, name, age)
        self.company = company

    def display_info(self):
        Person.display_info(self)
        print(f'Company: {self.company}')


class Student(Person):
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university

    def display_info(self):
        print(f'Student, {self.name}, studying at the university {self.university}')


people = [Person('Tom', 23), Student('Alice', 23, 'Harvard'), Employee('Rustem', 20, 'Google')]

for person in people:
    person.display_info()
    print()

