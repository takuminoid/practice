from abc import ABC, abstractmethod
import time


# class Sorter(ABC):
#     @abstractmethod
#     def sort(self, obj):
#         pass


# class QuickSorter(Sorter):
#     def sort(self, obj):
#         print("クイックソートでobjをソートする")


# class BubbleSorter(Sorter):
#     def sort(self, obj):
#         print("バブルソートでobjをソートする")


# class TimerSorter(Sorter):
#     def timer_sorter(self, obj):
#         start = time.time()
#         self.sort(obj)
#         end = time.time()
#         print("time:" + (end - start))


# 以下bridgeパターン
# 機能を拡張するためのクラス階層と実装を拡張するためのクラス階層を分ける
class SortImple(ABC):
    @abstractmethod
    def sort(self, obj):
        pass


class Sorter:
    def __init__(self, sort_imple: SortImple):
        self.sort_imple = sort_imple

    def sort(self, obj):
        self.sort_imple.sort(obj)


class QuickSorter(SortImple):
    def sort(self, obj):
        print("クイックソートでobjをソートする")


class BubbleSorter(SortImple):
    def sort(self, obj):
        print("バブルソートでobjをソートする")


class TimeSorter(Sorter):
    def __init__(self, sort_imple: SortImple):
        super().__init__(sort_imple)

    def time_sort(self, obj):
        start = time.time()
        self.sort(obj)
        end = time.time()
        print("time:" + (end - start))
