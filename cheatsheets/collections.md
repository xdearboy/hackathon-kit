# Коллекции

## `list`
Список подходит для упорядоченных данных.

- `append` — `O(1)` амортизированно
- `pop()` с конца — `O(1)`
- `pop(0)`, `insert(0, x)`, `remove(x)` — `O(n)`
- `x in lst` — `O(n)`
- срезы — `O(k)`, где `k` длина среза

```python
values = [1, 2, 3]
values.append(4)
last = values.pop()
```

Частые методы:

```python
values = [3, 1, 2]
values.extend([4, 5])
values.insert(1, 10)
values.remove(10)
values.reverse()
values.sort()
```

## `dict`
Словарь нужен для быстрых поисков по ключу.

- `get`, `setdefault`, `in` — в среднем `O(1)`
- удаление по ключу — в среднем `O(1)`

```python
scores = {"alice": 10, "bob": 15}
scores["carol"] = 7
print(scores.get("dave", 0))
```

Паттерны:

```python
words = ["a", "b", "a", "c"]
counts: dict[str, int] = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
```

```python
graph: dict[int, list[int]] = {}
graph.setdefault(1, []).append(2)
graph.setdefault(1, []).append(3)
```

## `set`
Множество хранит уникальные значения.

- `add`, `discard`, `in` — в среднем `O(1)`
- пересечение, объединение, разность — очень удобно для задач

```python
seen = {1, 2, 3}
seen.add(4)
seen.discard(2)
print(3 in seen)
```

Операции:

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # объединение
print(a & b)  # пересечение
print(a - b)  # разность
print(a ^ b)  # симметрическая разность
```

Когда удобно:

- убрать дубликаты;
- быстро проверять наличие;
- работать с пересечением множеств.

## `tuple`
Кортеж неизменяемый. Удобен для пар, ключей и возврата нескольких значений.

```python
point = (10, 20)
x, y = point
```

Ещё примеры:

```python
interval = (1, 10)
edges = {(1, 2), (2, 3)}
```

## Частые приёмы

```python
values = [5, 1, 5, 2]
unique_sorted = sorted(set(values))
counts: dict[int, int] = {}

for value in values:
    counts[value] = counts.get(value, 0) + 1

print(unique_sorted)
print(counts)
```

Шпаргалка по сложности:

- `list.append`, `list.pop()` с конца, `dict[key]`, `set.add` — обычно `O(1)`;
- `list.insert`, `list.remove`, `list.pop(0)` — `O(n)`;
- `dict` и `set` в среднем быстрые, но на худшем случае теоретически могут деградировать;
- если нужен порядок и быстрый доступ, часто берут `dict` + `list`.
