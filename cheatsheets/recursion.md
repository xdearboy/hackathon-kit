# Рекурсия

## Идея

Функция вызывает сама себя, пока не дойдёт до базового случая.

## Шаблон

```python
def solve(x: int) -> int:
    if x == 0:
        return 0
    return x + solve(x - 1)
```

## Базовый случай

Без него рекурсия уйдёт в бесконечность.

```python
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

## Типовые задачи

- обход дерева;
- DFS по графу;
- перебор вариантов;
- divide and conquer;
- работа с вложенными структурами.

## DFS на графе

```python
def dfs(graph: dict[int, list[int]], vertex: int, seen: set[int]) -> None:
    seen.add(vertex)
    for neighbor in graph.get(vertex, []):
        if neighbor not in seen:
            dfs(graph, neighbor, seen)
```

## Осторожно

- Python не любит слишком глубокую рекурсию;
- если глубина большая, смотри в сторону цикла и стека;
- перед сложной задачей убедись, что базовый случай один и понятный.

## Типичный шаблон для дерева

```python
def dfs(node) -> int:
    result = 1
    for child in node.children:
        result += dfs(child)
    return result
```
