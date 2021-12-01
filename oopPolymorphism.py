class Animal():
    species = 'mammal'

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')


class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"


class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"


# Example with function
def pet_speak(pet):
    print(pet.speak())


mydog = Dog(name='Judie')
mycat = Cat(name='Moorka')

print(mycat.speak())
print(mydog.speak())
print(type(mycat))

print(mycat.species)

