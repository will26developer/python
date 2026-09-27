

def square_digits(num: int) -> int:
    return int(''.join(str(int(num_str)**2) for num_str in str(num)))

print(square_digits(9119))