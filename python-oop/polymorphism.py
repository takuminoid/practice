class Dog:
    def cry(self):
        print("わんわん")


class Cat:
    def cry(self):
        print("ニャーニャー")


class Human:
    def cry(self):
        print("えーん")


def nake(animal):
    animal.cry()


dog = Dog()
cat = Cat()
human = Human()

nake(dog)
nake(cat)
nake(human)
