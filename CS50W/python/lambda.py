people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Syntherin"}
]


# def f(person):
#     return person["name"]
# people.sort(key=f)

# Using lambda instead of - because we jut need sort function and using one time
people.sort(key=lambda person:person["name"])

print(people)