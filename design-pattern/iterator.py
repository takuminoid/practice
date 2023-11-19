from abc import ABC, abstractmethod, abstractproperty


class Student:
    def __init__(self, name: str, sex: int):
        self._name = name
        self._sex = sex

    @property
    def name(self):
        return self._name

    @property
    def sex(self):
        return self._sex


class StudentList:
    def __init__(self):
        self._students = []

    @property
    def students(self):
        return self._students

    def add(self, student: Student):
        self._students.append(student)

    def get_student_at(self, index: int) -> Student:
        return self._students[index]

    def get_last_num(self) -> int:
        return len(self._students) - 1


class Teacher(ABC):
    def __init__(self, students_list: StudentList):
        self._students_list = students_list

    @abstractproperty
    def students_list(self):
        pass

    @abstractmethod
    def create_students_list(self, my_student: str):
        pass

    @abstractmethod
    def call_students(self):
        pass


class MyTeacher(Teacher):
    def __init__(self, students_list: StudentList):
        super().__init__(students_list)

    @property
    def students_list(self):
        return self._students_list

    def create_students_list(self, my_student: str):
        self._students_list.add(my_student)

    def call_students(self):
        for s in self._students_list.students:
            print(s.name)


if __name__ == "__main__":
    my_students_list = StudentList()
    you = MyTeacher(my_students_list)

    aoki = Student("青木亮太", 0)
    kamiya = Student("神谷里江", 1)
    sato = Student("佐藤美井", 1)
    tanaka = Student("田中未来", 0)
    nakai = Student("仲井新子", 1)

    you.create_students_list(aoki)
    you.create_students_list(kamiya)
    you.create_students_list(sato)
    you.create_students_list(tanaka)
    you.create_students_list(nakai)
    you.call_students()
