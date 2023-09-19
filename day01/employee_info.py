name = 'Azat'
age = 28
gender = 'M'
company = 'Google'
jobTitle = "SDET"
yearOfExperience = 1
salary = 100000
is_FullTime = True
is_Married = False
employee_id = 12345

name = input('Enter name:')
age = int(input('Enter age:'))
gender = input('Enter gender:')
company = input('Enter company name:')
jobTitle = input('Enter job title:')
salary = float(input('Enter your salary:'))

print(f'{name} is {age} years old, gender is {gender}\n'
      f'{name} works at {company} as a {jobTitle}\n'
      f'{name} makes $ {salary} per year')

