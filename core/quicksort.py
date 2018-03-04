import logging

from core.utils import swap_items

log = logging.getLogger(__name__)


def hoare_partition(l, lo, hi):
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
            swap_items(l, lo, right)
            return right
        else:
            # Swap misplaced items around pivot
            swap_items(l, left, right)


def quicksort(_list):
    if not _list:
        log.warning("Nothing to sort")

    def partition(l, lo, hi):
        return hoare_partition(l, lo, hi)

    def sort(l, lo, hi):
        if lo < hi:
            # Move pivot to its final position
            p = partition(l, lo, hi)
            # Sort elements left of partition
            sort(l, lo, p - 1)
            # Sort elements right of partition
            sort(l, p + 1, hi)
        return l

    return sort(_list, 0, len(_list) - 1)
