name = input('Enter your name:')
hourly_rate = float(input('Enter your hourly rate:'))
weekly_hours = int(input('How many hours you work in a week?'))
salary = hourly_rate * weekly_hours * 52

print(f'Hello {name}, your salary is $ {salary}')