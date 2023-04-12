import json

#x ='{ "name":"John", "age":30, "city":"New York"}'
with open('./resources/test.son','r') as f:
    x = f.read()


y = json.loads(x)
print(y)

print(y['age'])
print(y["city"])