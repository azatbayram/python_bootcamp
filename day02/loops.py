# For Loop
s = 'Python'

for each in s:
    print(each)

print('---------------------------')

for i in range(0, len(s)):
    print(s[i])

print('---------------------------')

for i in range(-len(s), 0):
    print(i)

print('---------------------------')

for i in range(-len(s), 0):
    print(s[i])

print('---------------------------')

for i in reversed(range(0, len(s))):
    print(s[i])

print('---------------------------')

for x in s[::-1]:
    print(x)

print('---------------------------')
# While Loop
num = int(input('Enter a positive number:\n'))

while num <= 0 :
    print('You entered invalid value!')
    num = int(input('Enter a positive number:\n'))

print(f'You have entered {num}')

print('---------------------------')

answer = input('Enter yes or no:\n')

while not (answer.lower() == 'yes' or answer.lower() == 'no'):
    print('You entered invalid value')
    answer = input('Enter yes or no:\n')

print(f'You have entered: {answer}')


