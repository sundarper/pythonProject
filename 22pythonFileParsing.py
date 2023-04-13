import os
with open('./resources/test.txt','r') as f: # no need to close the file
    lines = f.readlines()
    print(lines)

f = open ('./resources/test.txt','r') # need to close the file f.close()

contents = f.read()

print(contents)
f.close()

with open('./resources/test_new.txt','w') as f:
    f.write(contents)
    
