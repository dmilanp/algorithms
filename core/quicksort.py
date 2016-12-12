import logging
log = logging.getLogger(__name__)


def quicksort(_list):
    """An implementation of quicksort. Uses Hoare partition scheme"""

    if not _list:
        log.warning("Nothing to sort")

    def swap(l, a, b):
        l[a], l[b] = l[b], l[a]

    def partition(l, lo, hi):
        """Take first element and find its position somewhere between lo and hi, inclusive"""
        pivot = l[lo]
        left = lo + 1
        right = hi

        while True:
            # Advance left until finding a misplaced item
            while left <= (len(l) - 1) and l[left] <= pivot and left <= right:
                left += 1
            # Advance right until finding a misplaced item
            while right >= 0 and l[right] >= pivot and right >= left:
                right -= 1
            # If right is past left, swap pivot and return index
            if right < left:
                logging.debug("Moving pivot {} from index {} to {}".format(pivot, lo, right))
                swap(l, lo, right)
                return right
            else:
                # Swap misplaced items around pivot
                swap(l, left, right)

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
