import logging

from core.base_sort import BaseSort

log = logging.getLogger(__name__)


class QuickSort(BaseSort):

    def __init__(self, partition_method=None):
        super(QuickSort, self).__init__()
        self.partition = partition_method or self.hoare_partition

    def hoare_partition(self, l, lo, hi):
        pivot = l[lo]
        left = lo + 1
        right = hi

        while True:
            # Advance `left` until finding a misplaced item
            while left <= (len(l) - 1) and l[left] <= pivot and left <= right:
                left += 1
            # Regress `right` until finding a misplaced item
            while right >= 0 and l[right] >= pivot and right >= left:
                right -= 1
            if right < left:
                # Final position of pivot is `right`
                self.swap_items(l, lo, right)
                return right
            else:
                # Swap misplaced items around pivot
                self.swap_items(l, left, right)

    def _sort(self, l, lo, hi):
        if lo < hi:
            # Move pivot to its final position
            p = self.partition(l, lo, hi)
            # Sort elements left of partition
            self._sort(l, lo, p - 1)
            # Sort elements right of partition
            self._sort(l, p + 1, hi)
        return l

    def sort(self, _list):
        new_list = list(_list)
        return self._sort(new_list, 0, len(new_list) - 1)
