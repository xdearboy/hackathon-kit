# Классы

## Базовый OOP
Класс хранит данные и поведение. Используй, когда объект удобнее набора функций.

```python
class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Привет, {self.name}!"
```

База:

- `self` хранит состояние объекта;
- `__init__` вызывается при создании;
- методы работают с данными экземпляра.

## Dunder-методы
Нужны для красивого поведения объекта в Python.

```python
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)
```

Часто используют:

- `__repr__` — отладочное представление;
- `__str__` — пользовательский вывод;
- `__len__` — для `len(obj)`;
- `__iter__` — для циклов;
- `__getitem__` — для доступа по индексу;
- `__eq__` — для сравнения.

## Dataclasses
Быстрый способ описать контейнер данных.

```python
from dataclasses import dataclass


@dataclass(slots=True)
class Task:
    title: str
    priority: int
    done: bool = False
```

Плюсы:

- меньше шаблонного кода;
- автогенерация `__init__`, `__repr__`, `__eq__`;
- удобно для задач, где объект в основном хранит данные.

Полезные настройки:

```python
@dataclass(slots=True, frozen=True)
class User:
    name: str
    age: int
```

`slots=True` уменьшает память, `frozen=True` делает объект неизменяемым.

## Наследование
Используй, когда есть общая база и небольшие отличия.

```python
class Animal:
    def speak(self) -> str:
        return "..."


class Cat(Animal):
    def speak(self) -> str:
        return "meow"
```

Правила:

- выноси общее поведение в базовый класс;
- переопределяй только то, что реально отличается;
- если наследование притянуто за уши, чаще лучше композиция.

Пример с `super()`:

```python
class Person:
    def __init__(self, name: str) -> None:
        self.name = name


class Student(Person):
    def __init__(self, name: str, group: str) -> None:
        super().__init__(name)
        self.group = group
```

## Полезные паттерны

```python
class Counter:
    def __init__(self) -> None:
        self.value = 0

    def inc(self) -> int:
        self.value += 1
        return self.value


counter = Counter()
print(counter.inc())
```

Частые приёмы:

```python
class Box:
    def __init__(self) -> None:
        self.items: list[str] = []

    def add(self, item: str) -> None:
        self.items.append(item)

    def __len__(self) -> int:
        return len(self.items)
```
