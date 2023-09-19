number = int(input('Enter some integer number:'))
print(number)
if type(number) is int:
    if number%3 == 0:
        print('Buzz')
    elif number%5 == 0:
        print('FizzBuzz')
    else:
        print('Fizz')
else:
    print('Invalid input')
