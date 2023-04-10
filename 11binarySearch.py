low = 1
high  = 1000

num = int(input("Please enter the number : "))
print("Entered value :", num)
guess=0
while True:
    guess = guess+1
    mid = ((low + high) // 2)
    print("Mid ", mid)
    if num > mid:
        low = mid
    elif num < mid:
        high = mid
    else:
        print("Number found in {0} occurance".format(guess))
        break

