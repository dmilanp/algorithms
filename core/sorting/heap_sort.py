from core.sorting.base_sort import BaseSort
from structures.heap import Heap, max_heap


class HeapSort(BaseSort):

    def sort(self, _list):
        h = Heap(from_values=_list, heap_property=max_heap)
        sorted_list = []
        while h.heap:
            sorted_list.append(h.remove_root())

        return sorted_list[::-1]
