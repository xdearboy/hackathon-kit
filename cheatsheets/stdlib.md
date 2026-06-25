# Стандартная библиотека

## `collections`

### `deque`

Очередь и двусторонняя очередь.

```python
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)
queue.appendleft(0)
print(queue.popleft())
```

### `defaultdict`

Удобно для подсчёта и графов.

```python
from collections import defaultdict

counts = defaultdict(int)
for word in ["a", "b", "a"]:
    counts[word] += 1
```

### `Counter`

Подсчёт частот.

```python
from collections import Counter

counter = Counter("banana")
print(counter["a"])
```

## `heapq`

Мини-куча.

```python
import heapq

values = [5, 1, 3]
heapq.heapify(values)
heapq.heappush(values, 2)
print(heapq.heappop(values))
```

## `bisect`

Работа с отсортированными списками.

```python
from bisect import bisect_left, bisect_right

values = [1, 2, 2, 4, 7]
print(bisect_left(values, 2))
print(bisect_right(values, 2))
```

## `itertools`

```python
from itertools import product, permutations

print(list(product([1, 2], ["a", "b"])))
print(list(permutations([1, 2, 3], 2)))
```

## `functools`

### `lru_cache`

Кэш для рекурсивных функций.

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

## `math`

```python
from math import ceil, floor, isqrt

print(ceil(2.1))
print(floor(2.9))
print(isqrt(10))
```

## Когда брать стандартную библиотеку

- если готовое решение короче и понятнее;
- если не хочешь писать свой стек/очередь/кэш;
- если задача похожа на классическую олимпиадную.
