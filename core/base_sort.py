from __future__ import absolute_import, unicode_literals


class BaseSort(object):
    @staticmethod
    def swap_items(_list, a, b):
        # type: (list, int, int) -> None
        _list[a], _list[b] = _list[b], _list[a]
