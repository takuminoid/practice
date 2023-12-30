from abc import ABC, abstractmethod


class DirectoryEntry(ABC):
    @abstractmethod
    def remove(self):
        pass


class File(DirectoryEntry):
    def __init__(self, name: str):
        self.name = name

    def remove(self):
        print(self.name + "を削除しました")


class Directory(DirectoryEntry):
    def __init__(self, name: str):
        self.name = name
        self.list = []

    def add(self, file: File):
        self.list.append(file)

    def add(self, dir: "Directory"):
        self.list.append(dir)

    def remove(self):
        for l in self.list:
            if isinstance(l, DirectoryEntry):
                l.remove()
            else:
                print("削除できません")
        print(self.name + "を削除しました")


class SymbolicLink(DirectoryEntry):
    def __init__(self, name: str):
        self.name = name

    def remove(self):
        print(self.name + "を削除しました")


file1 = File("file1")
file2 = File("file2")
file3 = File("file3")
file4 = File("file4")
dir1 = Directory("dir1")
dir1.add(file1)
dir2 = Directory("dir2")
dir2.add(file2)
dir2.add(file3)
dir1.add(dir2)
dir1.add(file4)

dir1.remove()
