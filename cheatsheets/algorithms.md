# Алгоритмы

## Бинарный поиск
Используй для отсортированных массивов. Сложность: `O(log n)`.

```python
from bisect import bisect_left

values = [1, 3, 5, 7, 9]
target = 7

index = bisect_left(values, target)
if index < len(values) and values[index] == target:
    print(index)
else:
    print(-1)
```

Самописный вариант:

```python
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
```

Когда применять:

- поиск элемента в отсортированном массиве;
- поиск первого/последнего подходящего значения;
- задачи на минимальный ответ при монотонном условии.

Частые шаблоны:

```python
from bisect import bisect_left, bisect_right

values = [1, 1, 2, 2, 2, 5, 7]
left = bisect_left(values, 2)
right = bisect_right(values, 2)
count = right - left
```

```python
from collections.abc import Callable


def first_true(left: int, right: int, check: Callable[[int], bool]) -> int:
    while left < right:
        middle = (left + right) // 2
        if check(middle):
            right = middle
        else:
            left = middle + 1
    return left
```

## Сортировка
Нужна почти всегда. Базовые сложности:

- `sorted(...)`, `list.sort()` — `O(n log n)`
- `sorted(..., key=...)` — удобно для пар и структур

```python
values = [5, 1, 4, 2, 3]
values.sort()
print(values)

pairs = [(2, "b"), (1, "a"), (2, "a")]
print(sorted(pairs))
print(sorted(pairs, key=lambda item: (item[0], item[1])))
```

Полезные ключи:

```python
values = ["aaa", "b", "cc"]
print(sorted(values, key=len))

people = [("alice", 30), ("bob", 25), ("carol", 25)]
print(sorted(people, key=lambda item: (item[1], item[0])))
```

Совет:

- если нужен только минимум или максимум, сначала подумай про `min` и `max`, а не про сортировку;
- если нужно несколько раз искать элементы по порядку, один раз отсортируй и работай дальше через бинарный поиск.

## Решето Эратосфена
Для всех простых чисел на отрезке `[2..n]`. Сложность: `O(n log log n)`.

```python
def sieve(limit: int) -> list[int]:
    if limit < 2:
        return []

    is_composite = bytearray(limit + 1)
    primes: list[int] = []

    for number in range(2, limit + 1):
        if is_composite[number]:
            continue
        primes.append(number)
        start = number * number
        if start <= limit:
            is_composite[start : limit + 1 : number] = b"\x01" * ((limit - start) // number + 1)

    return primes
```

Памятка:

- `n < 2` — простых нет;
- старт вычёркивания идёт с `p * p`;
- для одной проверки простоты лучше `is_prime`, для списка простых — решето.

Ещё вариант для быстрых проверок:

```python
def build_prime_table(limit: int) -> list[bool]:
    table = [True] * (limit + 1)
    if limit >= 0:
        table[0] = False
    if limit >= 1:
        table[1] = False

    for number in range(2, isqrt(limit) + 1):
        if table[number]:
            for multiple in range(number * number, limit + 1, number):
                table[multiple] = False
    return table
```

## НОД и НОК
`gcd` и `lcm` часто нужны для дробей, периодов и делителей.

```python
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)
```

Использование:

```python
from math import gcd as math_gcd

numerator = 42
denominator = 56
divisor = math_gcd(numerator, denominator)
print(numerator // divisor, denominator // divisor)
```

```python
period1 = 12
period2 = 18
print(lcm(period1, period2))
```

## Два указателя
Подходит для отсортированных массивов, подотрезков и сканирования строки.

```python
values = [1, 2, 3, 4, 5, 6]
left = 0
right = len(values) - 1
target = 7

while left < right:
    current = values[left] + values[right]
    if current == target:
        print(left, right)
        break
    if current < target:
        left += 1
    else:
        right -= 1
```

Ещё два частых сценария:

```python
# Длина подотрезка без повторов
values = [1, 2, 1, 3, 2, 3, 4]
seen: set[int] = set()
left = 0
best = 0

for right, value in enumerate(values):
    while value in seen:
        seen.remove(values[left])
        left += 1
    seen.add(value)
    best = max(best, right - left + 1)
```

```python
# Скользящее окно по строке
s = "abacaba"
left = 0
window = {}

for right, char in enumerate(s):
    window[char] = window.get(char, 0) + 1
    while window[char] > 1:
        left_char = s[left]
        window[left_char] -= 1
        left += 1
```
