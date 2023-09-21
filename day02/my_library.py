import numbers

def square(num) -> numbers:
    return num * num

def cube(num) -> numbers:
    return square(num) * num

def print_each(sequence):
    for each in sequence:
        print(each)