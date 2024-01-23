from abc import ABC, abstractmethod


class Cuttable(ABC):
    pass


class Wood(Cuttable):
    def __str__(self):
        return "版木"


class Potato(Cuttable):
    def __str__(self):
        return "ジャガイモ"


class CutPrint(ABC):
    @abstractmethod
    def draw(self, hanzai: Cuttable):
        pass

    @abstractmethod
    def cut(self, hanzai: Cuttable):
        pass

    @abstractmethod
    def print(self, hanzai: Cuttable):
        pass

    # ここをoverrideすれば版材を変えられる
    def create_cuttable(self):
        return Wood()

    def create_cut_print(self):
        hanzai = self.create_cuttable()
        self.draw(hanzai)
        self.cut(hanzai)
        self.print(hanzai)


class ImagawasCutPrint(CutPrint):
    def draw(self, hanzai: Cuttable):
        print(str(hanzai) + "に漫画の絵を描く")

    def cut(self, hanzai: Cuttable):
        print(str(hanzai) + "に彫刻刀を利用して器用に彫る")

    def print(self, hanzai: Cuttable):
        print(str(hanzai) + "にインクとして、自分の血を使いプリントする")

    def create_cuttable(self):
        return Potato()


if __name__ == "__main__":
    imagawa = ImagawasCutPrint()
    imagawa.create_cut_print()
