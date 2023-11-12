# Displayクラスを継承するDecoDisplayクラスを定義する


class Display:
    def __init__(self):
        print("文章を出力できるよ")

    def display(self, sentence):
        print(sentence)


class DecoDisplay(Display):
    def display(self, sentence):
        print("~" + sentence + "~")


dis = Display()
dis.display("でデーン")
dec = DecoDisplay()
dec.display("デデーン！！")
