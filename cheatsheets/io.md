# Ввод и вывод

## Самый простой вариант

Если данные маленькие, используй обычный `input()`.

```python
n = int(input())
values = list(map(int, input().split()))
print(sum(values))
```

## Несколько строк

```python
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)
```

## Сбор ответа

Если ответов много, собирай их в список и печатай одним `print`.

```python
answers: list[str] = []

for _ in range(3):
    answers.append(input().strip())

print("\n".join(answers))
```

## Быстрый разбор строки

```python
line = input().strip()
parts = line.split()
numbers = list(map(int, parts))
```

## Когда нужен другой ввод

- если очень много данных, можно перейти на `sys.stdin.readline`;
- если вся задача в одной строке, обычного `input()` обычно хватает;
- если нужен потоковый разбор, часто делают `data = sys.stdin.read().split()`.

## Частые форматы

```python
n = int(input())
arr = list(map(int, input().split()))
```

```python
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
```

```python
s = input().strip()
t = input().strip()
```
