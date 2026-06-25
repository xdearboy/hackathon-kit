# Паттерн «Builder»

## Идея
Builder нужен, когда объект собирается по шагам и у него много опциональных частей.

## Пример

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

## Когда применять

- если создание объекта растянуто на несколько шагов;
- если хочется цепочку вызовов;
- если не хочется огромный `__init__`.
