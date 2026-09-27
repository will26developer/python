from typing import Any


def filter_list(list: list[Any]) -> list[int]:
    return [x for x in list if type(x) is int]

print(filter_list([1, 2, 'a','b']))