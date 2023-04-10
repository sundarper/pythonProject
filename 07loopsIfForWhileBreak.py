fruits = ['Apple', 'Orange', 'Banana', 'Peaches', 'cherry']
for i in fruits:
    if (i == 'Banana'):
        break
    print(i)
    for x in i:
        print(x)
print('%' * 10)
for i in fruits:
    if (i == 'Banana'):
        continue
    print(i)
print('*' * 10)

for i in range(1,6):
    print(i)
print('*' * 10)

for i in range(5, 30, 5):
    print(i)

for i in range(6):
    if (i == 3):
        break
    print(i)
else:
    print("Finally Finished!!!")


