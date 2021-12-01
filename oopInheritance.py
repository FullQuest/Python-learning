class Animal():

    def __init__(self):
        print('animal created')

    def who_am_i(self):
        print('i am an animal')

    def eat(self):
        print("i am eating")

myanimal = Animal()

myanimal.eat()
myanimal.who_am_i()


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")


    def who_am_i(self):
        print('I am a dog')


mydog = Dog()
mydog.eat()
mydog.who_am_i()


