
class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed


class Cat:
    def __init__(self,name,color):
        self.name=name
        self.color=color

dog1=Dog(name="Jerry",breed="German Shepherd")
cat1=Cat(name="Mau",color="Brown")

print(dog1.name)
print(dog1.breed)
print(cat1.color)