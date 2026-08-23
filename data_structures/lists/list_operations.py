fruits=["Apple","Banana","Pineapple"]

fruits[0]="Mango"

fruits.append("Cherry")

fruits.remove("Banana")

last=fruits.pop()
del fruits[0]
print(last)
print(fruits) #["Pineapple"]