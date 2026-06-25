# Паттерн «Singleton»

## Идея
Singleton оставляет один экземпляр класса на всё приложение.

## Пример

```python
class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.debug = False
        return cls._instance
```

## Когда применять

- если нужен один общий объект настроек;
- если состояние действительно должно быть общим;
- если задача прямо просит Singleton.
