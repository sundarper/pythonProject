
parrot = "Norwegian Blue"

for i in parrot:
    print(i)

varLst = parrot.split()
print(varLst)

varLst = parrot.split(' ')
print(varLst)

varLst = parrot.split('B')
print(varLst)

if 'lue' in varLst:
    print("Element Found in the List")

for i in varLst:
    print(i)

numbers = "9,223;372:036 854,755;807"
separators = ""
for i in numbers:
    if i.isnumeric():
        continue
    else:
        separators = separators + i
print(separators)

print('####'*10)
separators = numbers[1::4]  # if we know the pattern we can use this. 1 is starting position and 4 is next position
print(separators)

print('####'*10)
values = "".join(char if char not in separators else "," for char in numbers).split(",") # this return type is List because of Split
#values = "".join(char if char not in separators else "," for char in numbers) # this return type is String
print(values)
print(type(values))

#i if i not in separators else " " for i in numbers

myTuple = ("Sundar", "Valar", "Sundaresh", "Kamesh", "Sridevi")
x = "#".join(myTuple)
print(x)
print(type(x))

print('####'*10)
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)
print(type(x))





