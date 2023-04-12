"""
Given a square matrix, turn it by 90 degrees in a clockwise

Input:
1 2 3
4 5 6
7 8 9

Output:
7 4 1
8 5 2
9 6 3

Input:
1 2
3 4

Output:
3 1
4 2
"""
#output = [[7,4,1], [8,5,2], [9,6,3]]

def rotate_matrix(input):
    print("Len:", len(input))
    for i in range(len(input)):
        for j in range(i,len(input)):
            input[i][j],input[j][i] = input[j][i],input[i][j]
    for i in range(len(input)):
        input[i]=input[i][::-1]
    return input

input = [[1,2,3], [4,5,6], [7,8,9]]
#output = [[7,4,1], [8,5,2], [9,6,3]]
print(input[0])
print(input[0][::-1])
output = rotate_matrix(input)
print("Input :", input)
print("Output :", output)










