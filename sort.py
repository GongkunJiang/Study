import random, time, copy


class SelectionSort(object):
    items = []

    def __init__(self, items):
        self.items = items

    def sort(self):
        print("item len: %d" % len(self.items))
        for i in range(len(self.items) - 1, 0, -1):
            maximum = i
            for j in range(0, i):
                if (self.items[i] < self.items[j]):
                    maximum = j
            self.items[i], self.items[maximum] = self.swap(self.items[i], self.items[maximum])

    def swap(self, i, j):
        temp = j
        j = i
        i = temp
        return i, j


class InsertionSort(object):
    items = []

    def __init__(self, items):
        self.items = items

    def sort(self):
        for i in range(0, len(self.items)):
            j = i
            while (j > 0 and self.items[j] < self.items[j - 1]):
                # self.items[j],self.items[j-1] = self.swap(self.items[j],self.items[j-1])
                self.items[j], self.items[j - 1] = self.items[j - 1], self.items[j]
                j -= 1


def duration(sort_method):
    # calculate execution time for our selection sort method
    start = time.clock()
    sort_method.sort()
    end = time.clock()
    duration = end - start
    return duration


sizes = [
    1000,
    5000,
    10000
]

for size in sizes:
    # random generation of items to be sorted
    print("-" * 10 + "sorting numbers" + "-" * 10)
    items = []
    for i in range(0, size):
        items.append(random.randint(2, 999))
    # print "original items: %r" % items
    # the worse case
    items_worse = range(size - 1, -1, -1)
    # the best case
    items_best = range(0, size)

    to_be_sorted = [
        ("random case", items),
        ("worse case", items_worse),
        ("best case", items_best)
    ]

    for item in to_be_sorted:
        temp = copy.deepcopy(item)  # for reversing use after a certain sort
        print("-" * 10 + item[0] + "-" * 10)
        # calculate duration for insertion sort
        insertion_sort = InsertionSort(item[1])
        dinsertion = duration(insertion_sort)
        item = temp
        # calculate duration for selection sort
        selection_sort = SelectionSort(item[1])
        dselection = duration(selection_sort)
        item = temp
        # calculate duration for python builtin sort
        dpython = duration(item[1])
        print("%s: %ds" % ("insertion sort", dinsertion))
        print("%s: %ds" % ("selection sort", dselection))
        print("%s: %ds" % ("python built-in", dpython))
