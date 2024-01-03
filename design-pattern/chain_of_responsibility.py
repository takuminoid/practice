from abc import ABC, abstractmethod


class Responsible(ABC):
    def __init__(self, responsibler: str):
        self.responsibler = responsibler
        self.next = None

    def set_next(self, next_responsible: "Responsible"):
        self.next = next_responsible
        return next_responsible

    @abstractmethod
    def be_able_to_judge(self, question):
        pass

    @abstractmethod
    def judge(self, question):
        pass

    def put_question(self, question):
        if self.be_able_to_judge(question):
            self.judge(question)
        elif self.next is not None:
            self.next.put_question(question)
        else:
            print("誰にも判断できませんでした。やってみなさい！")


class ClassTeacher(Responsible):
    def __init__(self, responsibler: str):
        super().__init__(responsibler)
        self.responsible_level = Level(2)

    def be_able_to_judge(self, question):
        return question.level.less_than(self.responsible_level)

    def judge(self, question):
        print(self.responsibler + ": ok!!!")


class Student(Responsible):
    def __init__(self, responsibler: str):
        super().__init__(responsibler)
        self.responsible_level = Level(1)

    def be_able_to_judge(self, question):
        return question.level.less_than(self.responsible_level)

    def judge(self, question):
        print(self.responsibler + ": ok!!!")


class ChiefTeacher(Responsible):
    def __init__(self, responsibler: str):
        super().__init__(responsibler)
        self.responsible_level = Level(3)

    def be_able_to_judge(self, question):
        return question.level.less_than(self.responsible_level)

    def judge(self, question):
        print(self.responsibler + ": ok!!!")


class StaffMeeting(Responsible):
    def __init__(self, responsibler: str):
        super().__init__(responsibler)
        self.responsible_level = Level(4)

    def be_able_to_judge(self, question):
        return question.level.less_than(self.responsible_level)

    def judge(self, question):
        print(self.responsibler + ": ok!!!")


class Question:
    def __init__(self, content: str, level: int):
        self.content = content
        self.level = Level(level)

    def __str__(self):
        return self.content

    def get_level(self):
        return self.level


class Level:
    def __init__(self, level: "Level"):
        self.level = level

    def less_than(self, level: "Level"):
        if self.level <= level.level:
            return True
        else:
            return False


# Creating Responsible Chain
nakagawa = Student("Nakagawa")  # level1
rookie = ClassTeacher("Sato")  # level2
veteran = ChiefTeacher("Suzuki")  # level3
staff_meeting = StaffMeeting("職員会議")  # level4

# Setting up the Responsibility Chain
nakagawa.set_next(rookie).set_next(veteran).set_next(staff_meeting)

# Testing the Responsibility Chain
nakagawa.put_question(Question("おやつはいくらまで？", Level(1)))
nakagawa.put_question(Question("携帯電話持っていっていい？", Level(3)))
nakagawa.put_question(Question("がんばりましょ〜！", Level(5)))
