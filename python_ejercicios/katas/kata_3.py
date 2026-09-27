
def is_isogram(string: str) -> bool:
    lower_case_string: str = string.lower()
    count: int = 0
    for char in lower_case_string:
        if lower_case_string.count(char) > 1:
            count += 1
    return count == 0

print(is_isogram("WoNXUkPRVJBCUtrRCOyELjMiW"))