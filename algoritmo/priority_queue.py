def left(i):
    return 2*(i+1) - 1


def right(i):
    return 2*(i+1)


def parent(i):
    return (i+1)//2 - 1


def global_heapify(array, i, n, comp=lambda a, b: a < b):
    l = left(i)
    r = right(i)
    greatest = i
    if l < n:
        if comp(array[i], array[l]):
            greatest = l
        if r < n and comp(array[greatest], array[r]):
            greatest = r
    if greatest != i:
        array[greatest], array[i] = array[i], array[greatest]
        global_heapify(array, greatest, n, comp)


class Heap:
    def __init__(self, heap_array=[], comp=lambda a, b: a < b):
        self.comp = comp
        self.array = heap_array


    def empty(self):
        return len(self) == 0


    def insert(self, elem):
        self.array.append(elem)
        i = len(self.array)-1  
        p = parent(i)
        while i != 0 and self.comp(self.array[p], elem):
            self.array[i] = self.array[p]  
            i = p
            p = parent(p)
        self.array[i] = elem


    def heapify(self, i):
        global_heapify(self.array, i, len(self.array), self.comp)


    def top(self):
        return self.array[0]


    def pop(self):
        if len(self.array) == 0: return None
        max_ = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.heapify(0)
        return max_

    def not_empty(self):
        return len(self.array) > 0

    def __len__(self):
        return len(self.array)
