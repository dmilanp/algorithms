from core.base_sort import BaseSort


class InsertionSort(BaseSort):

    def sort(self, _list):
        l = list(_list)
        n = len(l)
        sorted_segment_end = 0

        for i in xrange(1, n):
            for j in xrange(i, 0, -1):
                if l[j-1] > l[j]:
                    self.swap_items(l, j-1, j)
                else:
                    break

            sorted_segment_end += 1

        return l
