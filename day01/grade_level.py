grade_level = int(input('Enter your garde level between 1 to 18:'))

if 1 <= grade_level <= 18:
    if 1 <= grade_level <= 5:
        print('Elementary School')
    elif 6 <= grade_level <= 8:
        print('Middle School')
    elif 9 <= grade_level <= 12:
        print('High School')
    elif 13 <= grade_level <= 16:
        print('Collage')
    elif 17 <= grade_level <= 18:
        print('Grad School')
else:
    print('Invalid grade level')
