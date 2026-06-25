# Задача: Singleton

## Условие
Нужен один общий объект настроек на всё приложение.

## Идея
Создать класс, который всегда возвращает один и тот же экземпляр.

## Решение

```python
class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.debug = False
        return cls._instance
```

## Проверка

```python
a = Settings()
b = Settings()
print(a is b)
```

## Важно

- в учебных задачах Singleton часто нужен только для понимания идеи;
- в реальном коде его лучше не использовать без причины;
- чаще удобнее передавать зависимости явно.
