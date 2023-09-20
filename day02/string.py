name = 'Python'

# forward indexes: 0, 1, 2, 3, 4, 5
# backward indexes: -6, -5, -4, -3, -2, -1

#length of string
print(len(name))

print(name[0])
print(name[len(name) - 1])
print(name[-1])

# string slicing(substring)
print(name[2:5])
word = 'Python Programming'
print(word[4:11])
print(word[:6])
print(word[7:])
print(word[::-1]) #reverses the string after slicing
s = str(reversed(name))
print(s)

print('---------------------------------------')

#string methods
print(word.upper()) # convert upper case
print(word.lower()) # convert lower case
print(word.capitalize()) # make first character upper case
print(word.title()) # make upper case first character of all word
print(word.split(' ')) # split string
print(word.startswith('P')) # check first character and return boolean
print(word.endswith(word[-1])) # check last character  and return boolean
print(word.isdigit()) # check string is digit
print(word.strip()) # trim in Java
print(word.index('n')) # return index of character
print(word.rindex('P'))
print(word.replace('Python', 'Java'))
print(word.replace('Python', 'C#'))

s = 'Java Java Java Python Python'
print(s.count('Java'))
print(s.count('Python'))

s2 = 'Java jAVA java JAVA Python python PYTHON'
print(s2.lower().count('java'))

s1 = 'java'
s2 = 'JAVA'

print(s1.lower() == s2.lower())

s3 = '4'
print(s3.isdigit())