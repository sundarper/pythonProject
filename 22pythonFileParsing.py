import os
with open('./resources/test.txt','r') as f:
    lines = f.readlines()
    print(lines)

f = open ('./resources/test.txt','r')

contents = f.read()

print(contents)
f.close()

with open('./resources/test_new.txt','w') as f:
    f.write(contents)
    
