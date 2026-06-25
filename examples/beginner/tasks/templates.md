# Шаблоны частых задач

## Строки

```python
def normalize(text: str) -> str:
    return " ".join(text.strip().lower().split())
```

## Массивы

```python
def prefix_sums(values: list[int]) -> list[int]:
    result = [0]
    for value in values:
        result.append(result[-1] + value)
    return result
```

## Два указателя

```python
def two_sum_sorted(values: list[int], target: int) -> tuple[int, int] | None:
    left = 0
    right = len(values) - 1

    while left < right:
        current = values[left] + values[right]
        if current == target:
            return left, right
        if current < target:
            left += 1
        else:
            right -= 1
    return None
```

## Жадные

```python
def choose_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    intervals = sorted(intervals, key=lambda item: item[1])
    result: list[tuple[int, int]] = []
    last_end = float("-inf")

    for start, end in intervals:
        if start >= last_end:
            result.append((start, end))
            last_end = end

    return result
```

## Графы

```python
from collections import deque


def bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    queue = deque([start])
    seen = {start}
    order: list[int] = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return order
```

## Динамика

```python
def fib(n: int) -> int:
    if n < 2:
        return n

    dp = [0, 1]
    for _ in range(2, n + 1):
        dp[0], dp[1] = dp[1], dp[0] + dp[1]
    return dp[1]
```
