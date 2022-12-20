data1 = (7, False, "Apple", True, 98.6)

print(len(data1))
print(data1[3])
print(data1.count(7))


data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}

print(data2.pop())
data2.add("Alpha")
print(data2)


data3 = ["A", 7, -1, 3.14, True, 7]

data3.reverse()
data3.insert(1, "B")
data3.pop()
print(data3)


data4 = {'name' : "Joe",  "age" : 26, "active" : True, "hourly_wage" : 14.75}


wages = data4["hourly_wage"] * 40
data4["active"] = False
data4["address"] = "123 West Main Street"
print(wages)
print(data4)