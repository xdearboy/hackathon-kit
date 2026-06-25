from math import isqrt


def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)


def binary_search(values: list[int], target: int) -> int:
    left = 0
    right = len(values) - 1
    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def sieve_of_eratosthenes(limit: int) -> list[int]:
    if limit < 2:
        return []

    is_composite = bytearray(limit + 1)
    primes = []

    for number in range(2, limit + 1):
        if is_composite[number]:
            continue
        primes.append(number)
        start = number * number
        if start <= limit:
            is_composite[start : limit + 1 : number] = b"\x01" * ((limit - start) // number + 1)

    return primes


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0:
        return False
    for divisor in range(3, isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True
