if False:
    print('Python Programming')

print('Java Programming')

print('--------------------------')

score = 70

if score >= 60:
    print('Congrats! You passed the exam')

"""
if(true){

}
"""

s = 'Hello World'

if 'H' and "W" in s:
    print(s, 'has', 'H and W')

print("------------------------------------------")

if score >= 60:
    print('Passed')
else:
    print('Failed')

print("------------------------------------------")

result = None
age = 20

if age >=21:
    result = 'eligible'
else:
    result = 'not eligible'

print(result)

print("------------------------------------------")

# Ternary

result='eligible' if score >= 21 else 'not eligible'

print(result)
print("------------------------------------------")

num = 100
result = None

if num > 0:
    result = 'positive'
elif num < 0:
    result = 'negative'
else:
    pass

print(result)

print("------------------------------------------")

result_2 = 'positive' if num > 0 else 'negative'

print(result_2)

print("------------------------------------------")

score = -300

if score >=0 and score <=100:
    if score >=60:
        print('Passed')
    else:
        print('Failed')
else:
    print("not valid score")

print("------------------------------------------")

score = 95

if 0 <= score <= 100:
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')
else:
    print('invalid score')