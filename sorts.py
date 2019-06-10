import abc


class Sorter(metaclass=abc.ABCMeta):
    def __init__(self, a_compare_method=lambda x, y: x < y):
        self.compare = a_compare_method

    @abc.abstractmethod
    def sort(self, arr):
        return arr


class MergeSorter(Sorter):
    def merge_sorted(self, arr1, arr2):
        """TODO base on iterators rather that mutators."""
        arr1, arr2 = list(arr1).copy(), list(arr2).copy()

        merged = []
        a = arr1.pop(0)
        b = arr2.pop(0)
        deleted = ''
        try:
            while True:
                deleted = ''
                if self.compare(a, b):
                    merged.append(a)
                    deleted = 'a'
                    a = arr1.pop(0)
                else:
                    merged.append(b)
                    deleted = 'b'
                    b = arr2.pop(0)
        except IndexError:
            merged.extend([b] + arr2 if deleted == 'a' else [a] + arr1)
        return merged

    def sort(self, arr):
        length = len(arr)
        return arr if length == 1 else self.merge_sorted(
            self.sort(arr[:length // 2]),
            self.sort(arr[length // 2:]),
        )


class BubbleSorter(Sorter):
    def sort(self, arr):
        try:
            while True:
                swapped = 'no'
                for i in range(len(arr)-1):
                    if self.compare(arr[i+1], arr[i]):
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                        swapped = 'yes'
                if swapped == 'no':
                    raise StopIteration
        except StopIteration:
            return arr
