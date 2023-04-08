a = "number is odd"
b = "number is even"
try:
    for i in range(1,100):
        if (i%2 == 0):
            print("After First Loop",b)
            for j in range(1,3):
                print("After Second Loop",b)
        else:
            print(a)
    print("#" * 80)
except:
    print("There is an error in the program")
finally:
    print("Executing final peice of code ")