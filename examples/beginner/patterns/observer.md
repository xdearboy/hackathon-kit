# Паттерн «Observer»

## Идея
Observer рассылает событие всем подписчикам.

## Пример

```python
class Subject:
    def __init__(self) -> None:
        self._observers = []

    def attach(self, observer) -> None:
        self._observers.append(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)


class Observer:
    def update(self, message: str) -> None:
        print(message)
```

## Когда применять

- если один объект влияет на несколько других;
- если нужна подписка на события;
- если нужно отделить источник события от реакции.
