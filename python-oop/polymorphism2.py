from abc import ABC, abstractmethod


class Worker(ABC):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("私の名前は" + self.name + "です")

    @abstractmethod
    def do_work(self):
        pass


class Teacher(Worker):
    def do_work(self):
        print(self.name + "は、教えた")


class Programmer(Worker):
    def do_work(self):
        print(self.name + "は、プログラミングをした")


def instract(worker):
    worker.do_work()


teacher = Teacher("John")
programmer = Programmer("Mike")
instract(teacher)
instract(programmer)
