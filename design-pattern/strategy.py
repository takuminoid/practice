from abc import ABC, abstractmethod


class Human:
    def __init__(self, name: str, height: int = -1, weight: int = -1, age: int = -1):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age


class Comparator(ABC):
    @abstractmethod
    def compare(self, h1: Human, h2: Human) -> int:
        pass


class AgeComparator(Comparator):
    def compare(h1: Human, h2: Human):
        if h1.age > h2.age:
            return 1
        elif h1.age == h2.age:
            return 0
        else:
            return -1


class HeightComparator(Comparator):
    def compare(self, h1: Human, h2: Human):
        if h1.height > h2.height:
            return 1
        elif h1.height == h2.height:
            return 0
        else:
            return -1


class MyClass:
    def __init__(self, comparator: Comparator):
        self.comparator = comparator

    def compare(self, h1: Human, h2: Human) -> int:
        return self.comparator.compare(h1, h2)


sato = Human("sato", 170, 60, 10)
takahashi = Human("takahashi", 150, 40, 20)
comparator = HeightComparator()
my_class = MyClass(comparator)
print(my_class.compare(sato, takahashi))
