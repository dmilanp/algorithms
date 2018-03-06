from core.sorting.base_sort import BaseSort


class SelectionSort(BaseSort):

    def sort(self, _list):
        l = list(_list)
        n = len(l)

        for i in xrange(n - 1):
            min_index = i
            for j in xrange(i, n):
                if l[j] < l[min_index]:
                    min_index = j
            self.swap_items(l, i, min_index)

        return l
