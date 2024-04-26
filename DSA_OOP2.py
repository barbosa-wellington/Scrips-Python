# inheretence

class Animal():

    def __init__(self):
        print("Animal created.")

    def printT(self):
        print("It is an animal.")

    def eat(self):
        print("It's time to eat")

    def sound(self):
        pass



class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Object Dog created.")

    def sound(self):
        print("Barking!")

class Cat(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Object Cat created.")

    def sound(self):
        print("Miah Miah")



Bilu = Dog()

Bilu.sound()


# Polymorphism

#Superclass
class vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def speeding(self):
        pass

    def braker(self):
        pass

#subclass