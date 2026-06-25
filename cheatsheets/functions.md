# Функции

## Определение

Функция нужна, когда один и тот же кусок логики хочется вызвать несколько раз.

```python
def add(a: int, b: int) -> int:
    return a + b
```

## Аргументы

```python
def greet(name: str, age: int = 18) -> str:
    return f"{name}: {age}"
```

```python
def join_words(*words: str) -> str:
    return " ".join(words)
```

```python
def make_user(**data: str) -> dict[str, str]:
    return data
```

## Возврат значения

Функция может вернуть одно значение, кортеж или `None`.

```python
def get_min_max(values: list[int]) -> tuple[int, int]:
    return min(values), max(values)
```

```python
def log_message(message: str) -> None:
    print(message)
```

## Рекурсия

Функция вызывает сама себя, если задача естественно раскладывается на подзадачи.

```python
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

## Лямбда

Короткая одноразовая функция, чаще всего для `key=`.

```python
values = [(2, "b"), (1, "a"), (3, "c")]
print(sorted(values, key=lambda item: item[0]))
```

## Полезные встроенные функции

```python
values = [1, 2, 3, 4]

print(sum(values))
print(min(values))
print(max(values))
print(len(values))
print(any(value > 3 for value in values))
print(all(value > 0 for value in values))
```

## Частые шаблоны

```python
def read_ints() -> list[int]:
    return list(map(int, input().split()))
```

```python
def solve() -> str:
    n = int(input())
    values = list(map(int, input().split()))
    return f"{sum(values[:n])}\n"
```

## Когда лучше делать функцию

- если логика повторяется;
- если хочется разбить задачу на маленькие части;
- если нужно проще тестировать код;
- если одна функция отвечает за одну понятную вещь.
