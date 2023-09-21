import numbers

class Employee:

    is_human = True # similar to static variable of Java
    planet = 'Earth'

    def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f'{self.name} is working as {self.job_title}')

    def __str__(self):
        # return f'Employee[name: {self.name}, job_title: {self.job_title}, salary: {self.salary}]'
        return f'{type(self).__name__}{self.__dict__}'

employee1 = Employee()
employee2 = Employee('Azat', 'SDET', 100000)
employee3 = Employee('Daniel')

print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

print('-------------------------')

print(employee2.name)
print(employee2.job_title)
print(employee2.salary)

print('-------------------------')

print(employee3.name)
print(employee3.job_title)
print(employee3.salary)

print('-------------------------')

print(Employee.is_human)
print(Employee.planet)

print('-------------------------')

employee1.work()
employee2.work()
employee3.work()

print('-------------------------')

print(employee2.__str__())