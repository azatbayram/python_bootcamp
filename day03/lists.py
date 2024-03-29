
groceries_list = ['Eggs', 'Milk', 'Rice']

# print list elements
print(groceries_list)

print('-------------------------')

#  add element to list
groceries_list.append('Chicken')
print(groceries_list)

print('-------------------------')

# insert the collection (multiple element) to list
groceries_list.extend(('Beef', 'Orange', 'Onion'))
print(groceries_list)

print('-------------------------')

# length of list
print(len(groceries_list))

print('-------------------------')

# update element
groceries_list[-2] = 'Cherry'
print(groceries_list)

print('-------------------------')

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers_list)
numbers_list[2:-2] = [300, 400, 500, 6]
print(numbers_list)

print('-------------------------')

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

list1 = characters[2: -3]
print(list1)

list2 = characters[:4]
print(list2)

list3 = characters[2:]
print(list3)

characters[2:5] = ['C', "D", 'E', 'C', 'D', 'E', 'X', 'Y', 'Z']
print(characters)

print('-------------------------')

names = ['Conor', 'Azat', 'Myrat', 'Ylyas', 'Hajy']

for x in names:
    print(x)

print('-------------------------')

nums = [10, 20, 30, 40, 50, 60]

for i in range(len(nums)):
    nums[i] = int(nums[i] / 5)

print(nums)

print('-------------------------')

for x in reversed(nums):
    print(x)

print('-------------------------')

print(nums[::-1])

print('-------------------------')

i = 0
while i < len(nums):
    print(nums[i])
    i += 1

print('-------------------------')

for i in range(1, 6):
    i += 2
    print(i)

print('-------------------------')

for i in reversed(range(len(nums))):
    print(nums[i])

print('-------------------------')

for x in nums[::-1]:
    print(x)

print('-------------------------')

# sort method
nums = [60, 500, 10, 20, 15, 5, 0]
nums.sort() # sorted ascending order
print(nums)

nums.sort(reverse=True) # sorted descending order
print(nums)

print('-------------------------')

# reverse method
list1 = [10, 20, 30, 40]
print(list1)
# print(list(reversed(list1)))
list1.reverse()
print(list1)

print('-------------------------')

tuple_elements = ('Java', 'Python', 'C#', 'Ruby')
print(tuple_elements)

list_elements = list(tuple_elements)
print(list_elements)
list_elements[-2] = 'C++'
list_elements.append('SWIFT')
print(list_elements)

tuple_elements = tuple(list_elements)
print(tuple_elements)

print('-------------------------')

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

print(list1 is list2)

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 3, 4, 5)

print(tuple1 is tuple2)

print('-------------------------')

print(groceries_list)

groceries_list.remove('Beef') # remove exact element
print(groceries_list)

groceries_list.pop() # remove last one
print(groceries_list)

groceries_list.pop(1)
print(groceries_list)

groceries_list.insert(2, 'Apple')
print(groceries_list)

print(groceries_list.index('Apple'))

nums = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1]

print(nums.count(1))

print('-------------------- Comprehensions -------------------------')
nums = []

for x in range(1, 51):
    nums.append(x)

print(nums)

print('------------------------------------')

"""
divisible_by_5 = []

for x in nums:
    if x % 5 == 0:
        divisible_by_5.append(x)

print(divisible_by_5)
"""

divisible_by_5 = [ x for x in nums if x % 5 == 0]
print(divisible_by_5)

print('------------------------------------')

even_nums = [ x for x in nums if x % 2 == 0]
odd_numbers = [x for x in nums if x % 2 != 0]

print(even_nums)
print(odd_numbers)

print('------------------------------------')

names = ['Python', 'Java', 'Java', 'JavaScript', 'java', 'JaVA', 'Ruby']

names = [x for x in names if x.lower() != 'java']

print(names)

