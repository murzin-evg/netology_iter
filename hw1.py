class FlatIterator:

    def __init__(self, list_of_list: list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.start = -1
        self.current = self.start
        self.end = len(self.list_of_list) - 1
        self.chunk = iter([])
        
        return self

    def __next__(self):
        try:
            item = next(self.chunk)

        except (StopIteration, TypeError):
            if self.current >= self.end:
                raise StopIteration
            
            self.current += 1

            if isinstance(self.list_of_list[self.current], (list, tuple)):
                self.chunk = iter(self.list_of_list[self.current])
                item = next(self.chunk)
            else:
                item = self.list_of_list[self.current]

        return item


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