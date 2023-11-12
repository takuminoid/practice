from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def cry(self):
        pass  # 抽象メソッドにはpassしか書けない


class Dog(Animal):
    def cry(self):
        print("わんわん")


class Cat(Animal):
    def cry(self):
        print("ニャーニャー")


class Monkey(Animal):
    def cry(self):
        print("キーキー")


monkey = Monkey()
monkey.cry()
