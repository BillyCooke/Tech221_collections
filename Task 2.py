story1 = {
    "Start": "The story starts of with an ordinary man in and ordinary life",
    "Middle": "One day, as he is walking down the street, a barrel of radioactive waste spills all over him and changes his physical form",
    "End": "He now has the ability to transform into any living creature and he uses this to protect others."
}
print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())
print(story1["Start"])
print(story1["Middle"])
print(story1["End"])

story1["Jeff"] = "Shapeshifter"
print(story1)