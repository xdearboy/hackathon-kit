# Паттерн «Strategy»

## Идея
Strategy позволяет менять алгоритм без переписывания клиента.

## Пример

```python
class NoDiscount:
    def apply(self, price: int) -> int:
        return price


class VipDiscount:
    def apply(self, price: int) -> int:
        return price - price // 10
```

## Когда применять

- если алгоритмов несколько;
- если хочется переключать поведение в рантайме;
- если нужно убрать ветвление из основного кода.
