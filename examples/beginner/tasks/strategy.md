# Задача: Strategy

## Условие
Есть корзина покупок. В зависимости от типа клиента скидка считается по-разному.

## Идея
Вынести алгоритм скидки в отдельные стратегии и подставлять их как объект.

## Решение

```python
class NoDiscount:
    def apply(self, price: int) -> int:
        return price


class VipDiscount:
    def apply(self, price: int) -> int:
        return price - price // 10


class StudentDiscount:
    def apply(self, price: int) -> int:
        return price - price // 5


class Cart:
    def __init__(self, strategy) -> None:
        self.strategy = strategy

    def total(self, price: int) -> int:
        return self.strategy.apply(price)
```

## Вывод

```python
cart = Cart(VipDiscount())
print(cart.total(1000))
```
