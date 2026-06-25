# Задача: Decorator

## Условие
Нужно добавить объекту новое поведение, не переписывая его класс.

## Идея
Обёртка хранит исходный объект и дополняет его поведение.

## Решение

```python
class Printer:
    def print_text(self) -> str:
        return "text"


class UppercasePrinter:
    def __init__(self, printer):
        self.printer = printer

    def print_text(self) -> str:
        return self.printer.print_text().upper()
```

## Когда удобно

- если нужно "обернуть" объект;
- если расширение поведения должно быть прозрачным;
- если нельзя менять исходный класс.
