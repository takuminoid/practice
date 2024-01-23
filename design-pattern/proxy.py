from abc import ABC, abstractmethod


class Teacher(ABC):
    @abstractmethod
    def answer_question1(self):
        pass

    @abstractmethod
    def answer_question2(self):
        pass

    @abstractmethod
    def answer_question3(self):
        pass


class Yamada(Teacher):
    def answer_question1(self):
        print("こうだよ")

    def answer_question2(self):
        print("これはね〜")

    def answer_question3(self):
        print("こうなんだよね〜")


class Fujiwara(Teacher):
    def __init__(self, senpai: Teacher):
        self.senpai = senpai

    def answer_question1(self):
        print("こうだよ")

    def answer_question2(self):
        print("これはね〜")

    def answer_question3(self):
        # Yamadaに聞く
        self.senpai.answer_question3()
        print("らしいよ")


class Student:
    def __init__(self, teacher: Teacher):
        self.teacher = teacher

    def ask_questions(self):
        self.teacher.answer_question1()
        self.teacher.answer_question2()
        self.teacher.answer_question3()


if __name__ == "__main__":
    yamada = Yamada()
    fujiwara = Fujiwara(yamada)
    s = Student(fujiwara)
    s.ask_questions()
