# break statement
for i in range(1, 10):
    print(i)
    if i == 5:
        break
print('---------------------')

# continue
for i in range(1, 11):
    if i == 3 or i == 7:
        continue # skip to the next iteration
    print(i)

print('---------------------')

# pass statement

for i in range(1, 11):
    if i == 3 or i == 7:
        pass
    print(i)
