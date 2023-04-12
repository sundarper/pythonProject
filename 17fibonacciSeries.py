
#def fibonacci_series(terms):
x1, x2 = 0, 1
print(x1, x2)
count = 0

terms = int(input("How many terms be to generate : "))
if terms <= 0:
    print("Please enter the Positive integer")
elif terms == 1:
    print(f"Fibonacci series upt  {terms} :")
    print(x1)
else:
    print("Fibonacci Series : ")
    # while count < terms:
    for i in range(terms):
        print(x1)
        nth = x1 + x2
        x1 = x2
        x2 = nth
     #   count += 1





#print(fibonacci_series(terms))

