from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, passport, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_passport(passport)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = passport
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('Фио должно быть строкой')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

        for s in f:
            if len(s) < 1:
                raise TypeError(' В фио должен быть хотя бы один символ')

            if len(s.strip(letters)) != 0:
                raise TypeError('Только буквы и дефис')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Возраст должен быть целым числом от 14 до 120')

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError('Вес должен быть больше 20')

    @classmethod
    def verify_passport(cls, passport):
        if type(passport) != str:
            raise TypeError('Паспорт должен быть в строковом формате')

        s = passport.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат записи')

        for p in s:
            if not p.isdigit():
                raise TypeError('Серия и номер должны быть числами')

        @property
        def fio(self):
            return self.__fio

        @property
        def old(self):
            return self.__old

        @old.setter
        def old(self, old):
            self.verify_old(old)
            self.__old = old

        @property
        def weight(self):
            return self.__weight

        @weight.setter
        def weight(self, weight):
            self.verify_old(old)
            self.__weight = weight

        @property
        def passport(self):
            return self.__passport

        @passport.setter
        def passport(self, passport):
            self.verify_passport(passport)
            self.__passport = passport


p = Person('Набиуллин Рустэм Рифович', 23, '1234 567891', 78.0)
print(p.__dict__)








