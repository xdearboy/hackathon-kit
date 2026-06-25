# Паттерн «Decorator»

## Идея
Decorator оборачивает объект и добавляет ему поведение снаружи.

## Пример

```python
class Printer:
    def print_text(self) -> str:
        return "text"


class UppercasePrinter:
    def __init__(self, printer) -> None:
        self.printer = printer

    def print_text(self) -> str:
        return self.printer.print_text().upper()
```

## Когда применять

- если нужно расширить поведение без изменения исходного класса;
- если декораторов может быть несколько;
- если важна композиция, а не наследование.
