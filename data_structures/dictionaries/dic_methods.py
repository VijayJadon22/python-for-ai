person = {"name": "Vijay","age":28, "city": "Gwalior", "role": "Full Stack Developer"}

print(person.keys())
print(person.values())
print(person.items())

if "name" in person:
    print("Name Found!")

person.update({"age":27,"job":"Engineer"})
print(person)

