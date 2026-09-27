

def dig_pow(n: int,p: int) -> int:
    num: int = sum(int(x)**(p+index) for index, x in enumerate(str(n)))
    return num // n if num % n == 0 else -1

print(dig_pow(46288,3))