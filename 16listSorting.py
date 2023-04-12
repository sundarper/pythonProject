
num = [100, 50000,200, 2000,30, 50, 1000, 50000,50000]

def lst_sorting(num):
    bignum = 0
    for i in range(len(num)):
        if bignum > num[i]:
            continue
        else:
            bignum = num[i]
    return bignum

print("Greate number : ", lst_sorting(num))

print(sorted(num)[-1]) # Greatest number

#print(sorted(num)[-3]) # Third largest number