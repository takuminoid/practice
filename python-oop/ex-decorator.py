# デコレータを使ってみる


def py(func):  # デコレータの定義
    def wrapper(*args, **kwargs):
        return "Pythonは" + func(*args, **kwargs)

    return wrapper


@py  # デコレータを利用
def obj():
    return "オブジェクト"


@py
def free(word):
    return word


class Hoge:
    @classmethod
    def foo(cls):  # インスタンスが入る場合はself, クラスが入る場合はcls
        print("インスタンス化しなくても呼び出せる")

    def bar(cls):
        print("呼び出せる？")


Hoge.foo()
Hoge().foo()
# Hoge.bar()
Hoge().bar()

# print(obj())
# print(free("楽しい"))
