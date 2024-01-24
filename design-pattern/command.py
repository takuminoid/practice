from abc import ABC, abstractmethod


class Beaker:
    def __init__(self, water: float, salt: float):
        self._water = water
        self._salt = salt
        self.mix()

        self._melted = True

    def add_salt(self, salt: float):
        self._salt += salt

    def add_water(self, water: float):
        self._water += water

    def mix(self):
        if (self.salt / (self.salt + self.water)) * 100 < 26.4:
            self._melted = True
        else:
            self._melted = False

    @property
    def salt(self):
        return self._salt

    @property
    def water(self):
        return self._water

    def is_melted(self):
        return self._melted

    def note(self):
        print(f"水: {self._water}g")
        print(f"食塩: {self._salt}g")
        print(f"濃度: {self._salt/(self._water+self._salt)*100}%")


class Command(ABC):
    def __init__(self, beaker: Beaker):
        self.beaker = beaker

    @abstractmethod
    def execute(self):
        pass


class AddSaltCommand(Command):
    def execute(self):
        print("食塩を1gずつ加える")
        while self.beaker.is_melted():
            self.beaker.add_salt(1)
            self.beaker.mix()
        self.beaker.note()


class MakeSaltWaterCommand(Command):
    def execute(self):
        print("食塩水を作る")
        self.beaker.mix()
        self.beaker.note()


class CompoundCommand(Command):
    def __init__(self, beaker: Beaker):
        super().__init__(beaker)

        self.commands: list[Command] = []

    def execute(self):
        for command in self.commands:
            command.execute()

    def add_command(self, command: Command):
        self.commands.append(command)


class Student:
    @staticmethod
    def do_experiment1():
        # 実験内容
        add_salt = AddSaltCommand(Beaker(100, 0))
        make_salt_water = MakeSaltWaterCommand(Beaker(0, 10))

        add_salt.execute()
        make_salt_water.execute()

    @staticmethod
    def do_experiment2():

        beaker = Beaker(90, 10)
        add_salt = AddSaltCommand(beaker)
        make_salt_water = MakeSaltWaterCommand(beaker)
        make_salt_water_add_salt = CompoundCommand(beaker)

        make_salt_water_add_salt.add_command(make_salt_water)
        make_salt_water_add_salt.add_command(add_salt)

        make_salt_water_add_salt.execute()


if __name__ == "__main__":
    print("1")
    Student.do_experiment1()
    print("2")
    Student.do_experiment2()
