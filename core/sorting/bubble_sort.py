from core.sorting.base_sort import BaseSort


class BubbleSort(BaseSort):

    def sort(self, _list):
        l = list(_list)
        n = len(l)

        for i in xrange(n - 1):
            for j in xrange(0, n - i - 1):
                if l[j] > l[j + 1]:
                    self.swap_items(l, j, j + 1)

        return l
