rich = ["mansion", "sports car", "helicopter", "speed boat", "jewellery"]
print(rich)
print(type(rich))

print("The first thing I would buy is a " + rich[0])
print("The second thing I would buy is a " + rich[1])
print("And I would also buy some " + rich[-1])

rich[0] = "multiple houses"
print("Actually I would buy " + rich[0] + " instead of one")
rich[1] = "luxury car"
print("I would also get a " + rich[1] + " instead")
print(rich)
rich.append("a business")
print(rich)
rich.remove("helicopter")
print(rich)
rich.pop()
print(rich)



