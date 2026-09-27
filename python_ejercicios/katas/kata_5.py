

def narcissistic(value: int) -> bool:
    num_str: str = str(value)
    sum_num: int = sum(int(num)**len(num_str) for num in num_str)
    return sum_num == value

print(narcissistic(153))