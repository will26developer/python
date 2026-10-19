
def is_prime(num):
    return num > 1 and num % num == 0 and num % 1 == 0


print(is_prime(4))