# Шаблон: классы как в тестовом задании

## Когда это нужно

Подходит для задач, где просят:

- сделать несколько связанных классов;
- использовать наследование;
- хранить состояние внутри объекта;
- добавить методы `get_*`, `set_*`, `change_*`.

## Идея

Сначала описываешь базовый класс с общими полями, потом наследника с дополнительными полями и методами.

## Базовый шаблон

```python
class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self._title = title
        self._author = author
        self._year = year
        self._is_borrowed = False

    def get_info(self) -> str:
        status = "borrowed" if self._is_borrowed else "available"
        return f"{self._title} | {self._author} | {self._year} | {status}"

    def borrow_book(self) -> None:
        self._is_borrowed = True

    def return_book(self) -> None:
        self._is_borrowed = False


class EBook(Book):
    def __init__(self, title: str, author: str, year: int, link: str, file_format: str) -> None:
        super().__init__(title, author, year)
        self._link = link
        self._format = file_format

    def get_format(self) -> str:
        return self._format

    def set_format(self, new_format: str) -> None:
        self._format = new_format
```

## Как писать `main.py`

```python
from library.book_module import Book, EBook


book = Book("Title", "Author", 2024)
ebook = EBook("Title", "Author", 2024, "https://example.com/book.pdf", "PDF")

print(book.get_info())
print(ebook.get_format())
```

## Что перенести из тестового задания

- приватные поля с подчёркиванием;
- отдельные методы для чтения и изменения данных;
- наследование через `super()`;
- простые строковые ответы без лишней логики;
- один объект = одна ответственность.

## Как быстро переделать под новую задачу

1. Выпиши, какие сущности есть в условии.
2. Найди общие поля и методы.
3. Вынеси их в базовый класс.
4. Всё, что отличается, положи в наследника.
5. В `main.py` просто создай объекты и вызови нужные методы.
