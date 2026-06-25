# Hackathon Kit

Короткий старт для Python-хакатона.

## Структура

- `cheatsheets/` — короткие русские шпоры по алгоритмам, коллекциям, строкам и классам
- `examples/` — примеры и мини-задачи для новичков
- `template/` — шаблон для боевых задач
- `tools/` — локальные утилиты для docstring
- `test_task/` — уже решённый референс-кейс

## Что использовать

- `uv` для запуска и окружения
- `ruff` для линта и форматирования
- `template/` как стартовый шаблон решения
- `cheatsheets/` как быстрые шпоры

## Быстрый старт

```bash
cd hackathon-kit/template
uv run python main.py < input.txt
```

Если нужно только проверить код:

```bash
cd hackathon-kit/template
uv run ruff check .
```

Форматирование:

```bash
cd hackathon-kit/template
uv run ruff format .
```

## Что внутри

- `template/main.py` — точка входа
- `template/src/solution.py` — класс `Solution` и процедурная версия
- `template/src/utils.py` — базовые функции для задач
- `cheatsheets/*.md` — короткие практичные шпаргалки
- `tools/docstring_report.py` — показать, где не хватает docstring
- `tools/docstring_skeleton.py` — сгенерировать skeleton docstring по сигнатурам
- `examples/beginner/patterns/adapter.md` — простой разбор паттерна Adapter для новичков
- `examples/beginner/tasks/*.md` — мини-оглавление задач по паттернам

## Docstring tools

Проверить проект на пропущенные docstring:

```bash
cd hackathon-kit
uv run python tools/docstring_report.py template/src
```

Сгенерировать заготовки для файла:

```bash
cd hackathon-kit
uv run python tools/docstring_skeleton.py template/src/solution.py
```

Если нужен внешний инструмент, чаще всего смотрят в сторону `docformatter`,
`pydocstyle` и `interrogate`. Для этого репо я добавил лёгкие локальные скрипты,
чтобы не зависеть от установки лишних пакетов.

## Автогенерация docstring

Готовой "идеальной" утилиты, которая понимает смысл кода и пишет хорошие docstring за тебя,
обычно нет. Практичный набор такой:

- `docformatter` — привести docstring к аккуратному виду;
- `interrogate` — найти места без docstring;
- `ruff` — подсветить правила стиля и часть docstring-проверок;
- `tools/docstring_skeleton.py` — быстро накинуть черновик docstring по сигнатурам.

## UV-команды

```bash
cd hackathon-kit
uv run python tools/docstring_report.py template/src
uv run python tools/docstring_skeleton.py template/src/solution.py
uv run ruff check template
uv run ruff format template
uv add --dev docformatter interrogate pydocstyle
uv run docformatter -i template/src/*.py
uv run interrogate template/src
```

## Pre-commit

```bash
cd hackathon-kit
uv run pre-commit install
uv run pre-commit run --all-files
```

Если `pre-commit` ещё не установлен в окружении:

```bash
cd hackathon-kit
uv add --dev pre-commit
```

## Перед GitHub

Чеклист перед публикацией:

- убедиться, что нет временных файлов и кэшей;
- оставить `README.md` как входную точку;
- проверить, что `.gitignore` покрывает `__pycache__`, `.ruff_cache`, `.venv`;
- при необходимости добавить `LICENSE` и `CONTRIBUTING.md`.

Если хочешь выложить это как отдельный репозиторий, достаточно:

```bash
git init
git add .
git commit -m "init hackathon kit"
```

## Template guide

Открой `template/README.md`, если нужен короткий пример, как быстро
подставить своё решение в шаблон.
