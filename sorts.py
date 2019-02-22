import abc


class Sort(metaclass=abc.ABCMeta):
    def __init__(self, a_compare_method):
        # TODO default compare method
        self.compare = a_compare_method

    @abc.abstractmethod
    def sort(self, arr):
        return arr


class Mergesort(Sort):
    # TODO unstatify
    @staticmethod
    def merge_sorted(arr1, arr2, compare):
        """TODO base on iterators rather that mutators."""
        arr1, arr2 = list(arr1).copy(), list(arr2).copy()

        merged = []
        a = arr1.pop(0)
        b = arr2.pop(0)
        deleted = ''
        try:
            while True:
                deleted = ''
                if compare(a, b):
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
            self.compare
        )


class Bubblesort(Sort):
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
