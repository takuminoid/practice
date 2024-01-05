# 既存のクラスを複数組み合わせて使う手順を「窓口」となるクラスを作ってシンプルに利用できるようにするパターン


class BookList:
    def search_book(self, book_name: str) -> str:
        book_storage = {"昆虫図鑑": "東1-3-501"}  # 本のリスト（例：configやdbから取得）
        return book_storage.get(book_name, "")  # 存在しない場合は空文字を返す


class LendingList:
    def __init__(self):
        self.lending_list = {}  # 貸し出しリスト

    def lend(self, book_name: str) -> None:
        self.lending_list[book_name] = True

    def return_book(self, book_name: str) -> None:
        self.lending_list[book_name] = False

    def is_lend(self, book_name: str) -> bool:
        return self.lending_list.get(book_name, False)


class LibraryFacade:
    def __init__(self):
        self.book_list = BookList()
        self.lending_list = LendingList()

    def search_book(self, book_name: str) -> str:
        location: str = self.book_list.search_book(book_name)
        if location != "":
            if self.lending_list.is_lend(book_name):
                return "貸出中"
            else:
                return location
        else:
            return "当図書館にはない"


class Visitor:
    def main(self):
        library = LibraryFacade()
        location: str = library.search_book("昆虫図鑑")
        if location == "貸出中":
            print("貸出中です")
        elif location == "当図書館にはない":
            print("当図書館にはありません")
        else:
            print(f"場所: {location}")


if __name__ == "__main__":
    visitor = Visitor()
    visitor.main()
