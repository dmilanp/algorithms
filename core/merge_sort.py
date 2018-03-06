from core.base_sort import BaseSort


class MergeSort(BaseSort):

    @staticmethod
    def merge_sorted(list_a, list_b):
        if not (list_a or list_b):
            return []

        if not list_a or not list_b:
            return list_a + list_b

        index_a = 0
        index_b = 0
        len_a = len(list_a)
        len_b = len(list_b)
        new_list = []

        while True:

            if index_a >= len_a and index_b >= len_b:
                break
            elif index_a >= len_a and index_b < len_b:
                new_list.append(list_b[index_b])
                index_b += 1
            elif index_a < len_a and index_b >= len_b:
                new_list.append(list_a[index_a])
                index_a += 1
            elif list_a[index_a] < list_b[index_b]:
                new_list.append(list_a[index_a])
                index_a += 1
            else:
                new_list.append(list_b[index_b])
                index_b += 1

        return new_list

    def sort(self, _list):
        l = list(_list)

        if len(l) == 1:
            return l

        l = self.merge_sorted(
            self.sort(l[:len(l)//2]),
            self.sort(l[len(l)//2:]),
        )
        return l
