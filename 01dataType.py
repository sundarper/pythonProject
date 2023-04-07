import datetime

print("This is Data Type Examples")
varStr = "this is my first \\n Data Type Examples"
print(varStr)
print("Type = type(varStr)")
varInt1 = 15
varInt2 = 20
varFlt1 = 5.9
varFlt2=4.7
varNone1 = None
varInt3 = varInt1+varInt2+varFlt1+int(varFlt2)
print(type(varFlt1))
print(varInt3)
varComp=10+110j
print(type(varComp))
varLst1=['abc',10,20,10,"sun", "python"]
print(varLst1)
print(type(varLst1))
varLst1.append("Rajan")
varLst1.append("Anand")
varLst1.remove('abc')
listLen = len(varLst1)
print("Lenght = " , listLen)
print(varLst1)

varTuple=('tuple','abc',10,20,10,"sun")
print(varTuple)
print(len(varTuple))
print(type(varTuple))

varSet={1,2, 55,2200, 10,'sundar', "anand", 60, 55,"Raj", 4}
print("Set :",varSet)
print(type(varSet))

varDict = {'name': 'Sundar', 'age':18}
print(varDict)
print(varDict.get('name'))
print("Age = ", varDict['age'])
print(type(varDict))
print(varDict.keys())
print(varDict.values())

import datetime
varDate = datetime.datetime.now()
print(varDate)
print(datetime.date)

