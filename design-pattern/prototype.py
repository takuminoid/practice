from abc import ABC, abstractmethod


# interface
class Cloneable(ABC):
    
    @abstractmethod
    def create_clone(self):
        pass

class Paper(Cloneable):
    
    def __init__(self):
        self.__name
    
    def paper(self):
        pass

    def paper(self, name):
        self.__name = name
    
    def create_clone(self) -> Cloneable:
        new_paper = Paper()
        new_paper.name = self.__name
        return new_paper


class Teacher():
    
    def create_many_crystals(self) -> list:
        prototype = Paper("雪の結晶")
        self.draw_crystal(prototype)
        self.cut_accordance_with_line(prototype)

        papers = [None] * 100

        for n in range(len(papers)):
            papers[n] = prototype.create_clone()
        
        return papers
    
    def _draw_crystal(self, paper: Paper):
        print('draw crystal')
        pass

    def _cut_accordance_with_line(self, paper: Paper):
        print('cut accordance with line')
        pass

class PrototypeKeeper():

    def __init__(self):
        self.__map = {}
    
    def add_cloneable(self, key: str, prototype: Cloneable):
        self.__map[key] = prototype
    
    def get_clone(self, key: str) -> Cloneable:
        prototype = self.__map[key]
        return prototype.create_clone()

