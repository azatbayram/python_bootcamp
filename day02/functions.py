import numbers

def display_message():
    print('here is your message')

display_message()

def value():
    return 10

print(value())

def string():
    return 'Hello Azat'

print(string())

def display_value(value):
    print(f'The value is {value}')

display_value(26)

def return_int() ->int:
    return 50

print(return_int())

def divide(num1, num2):
    return num1 / num2

def square(num: int):
    return num * num

print(divide(10, 2))
print(square(2))

#print(square('python'))

def addition(num1: numbers, num2: numbers) -> numbers:
    return num1+num2

print(addition(4, 7))
print(addition(2.3, 7.5))

print('---------------------------------------------')

def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator =='*':
        return  num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('invalid operator')
        return 0

print(calculate(8, 2, '+'))
print(calculate(8, 2, '-'))
print(calculate(8, 2, '*'))
print(calculate(8, 2, '/'))

print('---------------------------------------------')

# example of method overloading
def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    return n1 + n2 + n3 + n4


print(sum(4, 5))
print(sum(5, 6, 7))
print(sum(7, 3, 5, 2))

print('---------------------------------------------')

def concate(a: str, b, c = '', d = '', e = ''):
    print(f'{a} {b} {c} {d} {e}')

concate('Cydeo', 'School')
concate('Python', 'is', 7, True)

