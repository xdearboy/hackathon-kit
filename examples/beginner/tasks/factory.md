# Задача: Factory

## Условие
Есть несколько типов уведомлений: `email`, `sms`, `push`. Нужно создать объект по строковому типу, не размазывая `if` по всему коду.

## Идея
Фабрика принимает строку и возвращает нужный класс.

## Решение

```python
class EmailNotification:
    def send(self) -> str:
        return "Email sent"


class SmsNotification:
    def send(self) -> str:
        return "SMS sent"


class PushNotification:
    def send(self) -> str:
        return "Push sent"


class NotificationFactory:
    @staticmethod
    def create(kind: str):
        if kind == "email":
            return EmailNotification()
        if kind == "sms":
            return SmsNotification()
        if kind == "push":
            return PushNotification()
        raise ValueError(f"Unknown notification type: {kind}")
```

## Когда удобно

- когда создание объектов зависит от входной строки;
- когда хочется убрать длинные `if/elif` из основной логики;
- когда типы объектов часто расширяются.
