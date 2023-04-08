
varString1 = 5
print("The Number is {0}, squre is {1}, Cube is {2}" .format(varString1,varString1*varString1,varString1*varString1*varString1))
print("The Number is {0}, squre is {0}, Cube is {0}" .format(varString1,varString1*varString1,varString1*varString1*varString1))
print("The Number is {0}, squre is {0}, Cube is {2}" .format(varString1,varString1*varString1,varString1*varString1*varString1))

#No  Alignment
for i in range(13):
    print("The Number is {0}, squre is {1}, Cube is {2}".format(i, i * i,
                                                                i * i * i))
    print(f"The Number is {i}, squre is {i*i}, Cube is {i*i*i}")

pi = 22/7
print("pi is {0}" .format(pi))
print("pi is {0:12}" .format(pi)) # this means value will be of 12 chr in total. if the value shorter than 12 char ie it will be right aligned
print("pi is {0:12f}" .format(pi)) # this means value will be of 12 chr in total. But f means there will be a decimal values and by default it will be 6.the remaining lenght will be filled by leading spaces
print("pi is {0:12.50f}" .format(pi))
#Right Alignment
print("pi is {0:52.50f}" .format(pi))
print("pi is {0:62.50f}" .format(pi))
print("pi is {0:55.2f}" .format(pi))

#Left Alignment
for i in range(13):
    print("The Number Left align {0:2}, squre is {1:<3}, Cube is {2:4}".format(i, i * i,
                                                                i * i * i))

