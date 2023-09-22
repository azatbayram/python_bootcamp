class Person:

    def __init__(self, name: str = 'Unknown', age: int = 0):
        self.__name = None
        self.__age = None
        self.set_name(name)
        self.set_age(age)

    def get_name(self) -> str:

        if self.__name == None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f'Invalid name: {self.__name}')

        return self.__name

    def set_name(self, name: str):

        if type(name) != str:
            raise RuntimeError(f'Person name must be string')

        if name == '':
            raise RuntimeError(f'Person name can not be empty')

        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):

        if age < 0 or age > 150:
            raise RuntimeError(f'Invalid age: {age}')

        self.__age = age

    def __str__(self) -> str:
        return f'{type(self).__name__}{ str(self.__dict__).replace("_Person__", "")}'


person1 = Person()
person1.set_name('Azat')
print(person1.get_name())
print(person1.get_age())

person2 = Person('James')

print(person2.get_name())
print(person2.get_age())


person3 = Person('Hazel', 27)

print(person3.get_name())
print(person3.get_age())

print('------------------')

print(person1)
print(person2)
print(person3)