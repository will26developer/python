from typing import Any


def remove_duplicates(array: list[Any]) -> list[Any]:
    checked: set[Any] = set()
    new_array: list[Any] = []
    for i in array:
        if i not in checked:
            checked.add(i)
            new_array.append(i)
    return new_array


print(remove_duplicates([4, 8, 2, 8, 5, 4, 9, 2, 1, 5, 8, 3, 9, 4, 6]))