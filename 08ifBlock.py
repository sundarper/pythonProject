
# name = input("Please enter the Name:")
# age = int(input("Please enter the Age:"))
#
# if (age > 18):
#     print("Your good enough to Vote !!!")
# elif (age == 18):
#     print("Congrats you just turned 18 allowed to Vote !!!")
# else:
#     print("you will allowed to vote in {0} year".format(18-age))
# print("*"*25)
#
# day = "Friday"
# temp = 27
# raining = False
# if(day == "Saturday") and (temp < 27) or not raining:
#     print("Go swiming ")
# else:
#     print("Learn Python")
#
# day = "Friday"
# temp = 27
# raining = True
# if (day == "Saturday" and temp < 27) or not raining:
#     print("Go swiming ")
# else:
#     print("Learn Python")
#
# if 0:
#     print ("True")
# else:
#     print ("False")
#
# name = input("Please enter the Name:")
# if name:
#     print("True")
# else:
#     print("False")

print("*"*25)

parrot = "Norwegian Blue"
letter = input("Please enter the Letter : ")
if letter in parrot:
    print("Found")
else:
    print("Not Found")

if letter.casefold() in parrot.casefold():
    print("Found")
else:
    print("Not Found")










