

def count(s: str) -> dict[str, int]:
    if s == "":
        return {}
    map_word: dict[str, int] = dict.fromkeys(s, 0)
    for char in s:
        map_word[char] = s.count(char)
    return map_word

print(count("aba"))