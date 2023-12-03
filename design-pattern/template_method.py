from abc import ABC, abstractmethod


class Cuttable(ABC):
    pass


class Wood(Cuttable):
    def __str__(self):
        return "版木"


class WoodCutPrint(ABC):
    @abstractmethod
    def draw(self, hanzai: Cuttable):
        pass

    @abstractmethod
    def cut(self, hanzai: Cuttable):
        pass

    @abstractmethod
    def print(self, hanzai: Cuttable):
        pass

    def create_wood_cut_print(self):
        hanzai = Wood()
        self.draw(hanzai)
        self.cut(hanzai)
        self.print(hanzai)


class TanakasWoodCutPrint(WoodCutPrint):
    def draw(self, hanzai: Cuttable):
        print(str(hanzai) + "にマジックを使って大好きな女の子の絵を描く")

    def cut(self, hanzai: Cuttable):
        print("彫刻刀を使って細部まで丁寧に" + str(hanzai) + "を彫る")

    def print(self, hanzai: Cuttable):
        print("版画インクを使って豪快にプリントする")


if __name__ == "__main__":
    tanakas = TanakasWoodCutPrint()
    tanakas.create_wood_cut_print()
