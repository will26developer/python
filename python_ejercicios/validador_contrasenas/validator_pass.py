import string


def validate_password(password: str) -> bool:
    there_upper = False
    min_len = False
    there_digit = False
    there_punctuation = False
    there_lower = False
    if  len(password) >= 8:
        min_len = True
        for char in password:
            if char.isupper():
                there_upper = True
            if char.isdigit():
                there_digit = True
            if char in string.punctuation:
                there_punctuation = True
            if char.islower():
                there_lower = True
    return there_upper and there_digit and there_punctuation and min_len and there_lower

print(validate_password("Overkill@7698"))