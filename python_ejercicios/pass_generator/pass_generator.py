from secrets import choice
from string import ascii_letters, digits, punctuation

def pass_generator(long: int) -> str:
    chain: str = ascii_letters + digits + punctuation
    return "".join(choice(chain) for _ in range(long))

print(pass_generator(10))