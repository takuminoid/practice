# 処理と処理対象を分け処理の追加を容易にする

from abc import ABC, abstractmethod


class Home(ABC):
    @abstractmethod
    def praised_child(self):
        pass

    @abstractmethod
    def reproved_child(self):
        pass


class Tea:
    pass


class Teacher(ABC):
    @abstractmethod
    def visit(self, student_home: Home):
        pass

    @abstractmethod
    def visit(self, student_home: "TanakaHome"):
        pass

    @abstractmethod
    def visit(self, student_home: "SuzukiHome"):
        pass

    def get_student_list(self):
        return self.students


class RookieTeacher(Teacher):
    def __init__(self, students: list):
        self.students = students

    def visit(self, student_home):
        if isinstance(student_home, SuzukiHome):
            student_home.reproved_child()
        elif isinstance(student_home, TanakaHome):
            student_home.praised_child()
        elif isinstance(student_home, Home):
            print("Hello")
        else:
            print("知らない家です")


class TeacherAcceptor(ABC):
    def accept(self, teacher: Teacher):
        pass


class SuzukiHome(Home, TeacherAcceptor):
    def praised_child(self):
        print("あら、先生ったらご冗談を")
        return Tea()

    def reproved_child(self):
        print("うちの子に限って...")
        return

    # 訪問者を受け入れるメソッド
    def accept(self, teacher: Teacher):
        teacher.visit(self)


class TanakaHome(Home, TeacherAcceptor):
    def praised_child(self):
        print("あら、先生ったらご冗談を")
        return Tea()

    def reproved_child(self):
        print("tanaka kenji うちの子に限って...")
        return

    # 訪問者を受け入れるメソッド
    def accept(self, teacher: Teacher):
        teacher.visit(self)


taro = SuzukiHome()
kenji = TanakaHome()
students = [taro, kenji]
sato = RookieTeacher(students)
taro.accept(sato)
kenji.accept(sato)
