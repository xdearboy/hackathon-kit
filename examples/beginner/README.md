# Beginner Examples

Здесь лежат короткие разборы типовых задач и паттернов.

## Оглавление

### Паттерны

- `patterns/README.md` — оглавление всех паттернов
- `patterns/adapter.md` — паттерн Adapter на простом примере с ноутбуком и проектором
- `patterns/builder.md` — Builder с пошаговой сборкой объекта
- `patterns/decorator.md` — Decorator как обёртка поведения
- `patterns/facade.md` — Facade как один простой вход
- `patterns/factory.md` — Factory для создания объектов по типу
- `patterns/observer.md` — Observer для подписки на события
- `patterns/singleton.md` — Singleton для одного общего экземпляра
- `patterns/strategy.md` — Strategy для смены алгоритма

### Задачи

- `tasks/README.md` — оглавление всех beginner-задач
- `tasks/adapter.md` — адаптер для HDMI и USB-C
- `tasks/decorator.md` — декоратор как обёртка поведения
- `tasks/observer.md` — уведомление подписчиков
- `tasks/builder.md` — пошаговая сборка объекта
- `tasks/facade.md` — один простой интерфейс поверх подсистем
- `tasks/factory.md` — фабрика уведомлений
- `tasks/strategy.md` — стратегии скидок
- `tasks/singleton.md` — один объект настроек на всё приложение
- `tasks/oop_book.md` — классы и наследование в стиле тестового задания
- `tasks/templates.md` — шаблоны для строк, массивов, графов, DP и жадных

## Как пользоваться

Открой нужную задачу, выпиши идею в 2–3 строки, потом перепиши код под условие.

## UV-команды

```bash
cd hackathon-kit
uv run python tools/docstring_report.py template/src
uv run python tools/docstring_skeleton.py template/src/solution.py
uv run ruff check template
uv run ruff format template
```

Если надо поставить внешние утилиты для docstring:

```bash
cd hackathon-kit
uv add --dev docformatter interrogate pydocstyle
uv run docformatter -i template/src/*.py
uv run interrogate template/src
```
