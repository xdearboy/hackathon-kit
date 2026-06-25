# Задача: Builder

## Условие
Нужно собирать сложный объект по шагам.

## Идея
Отдельный билдер накапливает параметры и потом создаёт итоговый объект.

## Решение

```python
class Pizza:
    def __init__(self, cheese: bool = False, pepperoni: bool = False) -> None:
        self.cheese = cheese
        self.pepperoni = pepperoni


class PizzaBuilder:
    def __init__(self) -> None:
        self.cheese = False
        self.pepperoni = False

    def add_cheese(self) -> "PizzaBuilder":
        self.cheese = True
        return self

    def add_pepperoni(self) -> "PizzaBuilder":
        self.pepperoni = True
        return self

    def build(self) -> Pizza:
        return Pizza(self.cheese, self.pepperoni)
```

## Когда удобно

- если объект создаётся в несколько шагов;
- если хочется читаемый chain-call стиль;
- если у объекта много опциональных параметров.
