# Задача: Observer

## Условие
Есть объект-источник событий. Несколько подписчиков должны реагировать на изменения.

## Идея
Источник хранит список наблюдателей и уведомляет их при изменении.

## Решение

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

## Когда удобно

- если одно изменение должно разойтись в несколько мест;
- если нужно подписываться на события;
- если хочется отделить источник от реакции.
