import abc


class Sorter(metaclass=abc.ABCMeta):
    def __init__(self, a_compare_method=lambda x, y: x < y):
        self.compare = a_compare_method

    @abc.abstractmethod
    def sort(self, arr):
        return arr


class MergeSorter(Sorter):
    def merge_sorted(self, arr1, arr2):
        iter1, iter2 = iter(arr1), iter(arr2)
        merged = []

        try:
            a = next(iter1)
        except StopIteration:
            return arr2
        try:
            b = next(iter2)
        except StopIteration:
            return arr1

        delete_trial = ''
        try:
            while True:
                delete_trial = ''
                if self.compare(a, b):
                    merged.append(a)
                    delete_trial = 'a'
                    a = next(iter1)
                else:
                    merged.append(b)
                    delete_trial = 'b'
                    b = next(iter2)
        except StopIteration:
            merged.extend([b] + list(iter2) if delete_trial == 'a' else [a] + list(iter1))
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
