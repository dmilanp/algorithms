import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger(__name__)


def max_heap(parent, child):
    return parent >= child


def min_heap(parent, child):
    return parent <= child


def swap_items(_list, a, b):
    # type: (list, int, int) -> None
    _list[a], _list[b] = _list[b], _list[a]


class Heap(object):

    def __init__(self, from_values=[], heap_property=max_heap):
        super(Heap, self).__init__()
        assert heap_property in [max_heap, min_heap]
        self.heap = from_values
        self.heap_property = heap_property

        try:
            self.check_heap_property()
        except AssertionError:
            logging.warning(
                'Provided values do not hold {} property. Correcting heap...'.format(self.heap_property.__name__)
            )
            self.correct_heap()
            logging.info('New heap is {}'.format(self.heap))

    def check_heap_property(self):
        for i in xrange(len(self.heap)):
            for child in filter(lambda index: index < len(self.heap), [2*i+1, 2*i+2]):
                assert self.heap_property(parent=self.heap[i], child=self.heap[child]), \
                'Parent at {} (value={}) and child at {} (value={}) violate the {} property'.format(
                    i, self.heap[i], child, self.heap[child], self.heap_property.__name__,
                )

    def insert(self, value):
        self.heap.append(value)
        new_value_index = len(self.heap) - 1
        parent_index = self.get_parent_index(new_value_index)

        while not self.heap_property(parent=self.heap[parent_index], child=self.heap[new_value_index]):
            swap_items(self.heap, new_value_index, parent_index)
            new_value_index = parent_index
            parent_index = self.get_parent_index(new_value_index)

            if parent_index == -1:
                break

    def _remove_strategy(self):
        """
        When removing the root element, we replace it with the last one and bubble it down.
        In max_heap case we replace it with the maximum of the children, whereas in case of min_heap we replace
        it with the minimum.
        """
        if self.heap_property == max_heap:
            return max
        else:
            return min

    def remove_root(self):
        if len(self.heap) <= 1:
            self.heap = []
            return

        swap_items(self.heap, 0, len(self.heap) - 1)
        self.heap.pop(len(self.heap) - 1)
        cmp_fn = self._remove_strategy()

        moved_item_index = 0
        children = [index for index in self.get_child_indices(moved_item_index) if index < len(self.heap)]

        while children:
            children_values = [self.heap[index] for index in children]
            next_candidate = cmp_fn(children_values)

            if self.heap_property(parent=self.heap[moved_item_index], child=next_candidate):
                break

            next_candidate_index = self.heap.index(next_candidate)
            swap_items(self.heap, moved_item_index, next_candidate_index)
            moved_item_index = next_candidate_index
            children = [index for index in self.get_child_indices(moved_item_index) if index < len(self.heap)]

    def get_parent_index(self, child_index):
        assert child_index >= 0, 'Child index cannot be negative'

        if child_index == 0:
            return -1

        if child_index % 2 == 0:
            return (child_index - 2) / 2
        else:
            return (child_index - 1) / 2

    def get_child_indices(self, index):
        return index*2+1, index*2+2

    def correct_heap(self):
        old_heap = list(self.heap)
        self.heap = []

        for item in old_heap:
            self.insert(item)
