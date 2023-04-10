
varList = ["CPU", "RAM", "SSD", "Monitor", "Keybord", "Mouse"]

print(varList[2])
varList.append("Motherbord")
print(varList)
varList[4] = "Kyeboard"
print(varList)
varList.remove("SSD")
print(varList)
del varList[4]
print(varList)

print(varList[-1])
print(varList[1:4])

