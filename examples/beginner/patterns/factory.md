# Паттерн «Factory»

## Идея
Factory создаёт нужный объект по параметру и убирает создание из основной логики.

## Пример

```python
class EmailNotification:
    def send(self) -> str:
        return "Email sent"


class SmsNotification:
    def send(self) -> str:
        return "SMS sent"


class NotificationFactory:
    @staticmethod
    def create(kind: str):
        if kind == "email":
            return EmailNotification()
        if kind == "sms":
            return SmsNotification()
        raise ValueError(kind)
```

## Когда применять

- если тип объекта зависит от строки, числа или флага;
- если не хочется `if/elif` по всему проекту;
- если типы объектов часто расширяются.
