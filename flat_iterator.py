
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.index = -1

    def __iter__(self):
        self.index += 1
        self.next_index = 0
        self.len_list = len(self.list_of_list)
        return self

    def __next__(self):
        if self.index == self.len_list:
            raise StopIteration
        el = self.list_of_list[self.index][self.next_index]
        self.next_index += 1
        if self.next_index == len(self.list_of_list[self.index]):
            iter(self)

        return el


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()