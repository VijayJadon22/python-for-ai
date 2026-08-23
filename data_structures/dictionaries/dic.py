my_dict={}

person={
    "name":"Alice",
    "age":28,
    "city":"Gwalior"
}


age=person["age"]
print(age)

person["name"]="Vijay"
person["role"]="Full Stack Developer"
del person["age"]
print(person)
