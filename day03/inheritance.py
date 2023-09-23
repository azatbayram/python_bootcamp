class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'

class Employee(Person):

    def __init__(self, name: str, age: int, job_title: str, company_name: str = 'Unknown', salary: int = 0):
        super().__init__(name, age) # calling parent class constructor
        self.job_title = job_title
        self.company_name = company_name
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')
        
class Developer(Employee):

    def work(self):
        print(f'{self.job_title} {self.name} is coding')


class Teacher(Employee):

    def __init__(self, name: str, age: int, job_title: str = 'Teacher', company_name: str = 'Unknown', salary: int = 0):
        super().__init__(name, age, job_title, company_name, salary)


    def work(self):
        print(f'{self.name} is teaching')



employee = Employee('Hazel', 25, 'QA', 'Apple Inc')
developer = Developer('Azat', 28, 'Developer', 'Google Inc', 100000)
teacher = Teacher('Myrat', 35)

employee.work()
print(employee.__str__())
print('-------------------------------')
developer.work()
print(developer.__str__())
print('-------------------------------')
teacher.work()
print(teacher.__str__())