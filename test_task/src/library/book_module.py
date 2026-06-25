from datetime import datetime


class Book:
    """
    Класс Book

    Свойства:
        _title - название книги
        _author - автор
        _year - год издания
        _is_borrowed - статус взятия
        _borrow_date - дата взятия
        _borrow_period_days - срок займа (по умолчанию 14 дней)

    Методы:
        get_info() - возвращает строку с полной информацией о книге
        get_title() / set_title() - получить/изменить название
        get_author() / set_author() - получить/изменить автора
        get_year() / set_year() - получить/изменить год
        borrow_book() - взять книгу взаймы (если свободна)
        return_book() - вернуть книгу
        is_borrowed() - проверить статус
        extend_borrow_period() - продлить срок займа
        change_author() - изменить автора
        get_age() - узнать возраст книги
    """

    def __init__(self, title, author, year):
        """
        Аргументы:
            title (str): название книги
            author (str): автор книги
            year (int): год
        """
        self._title = title
        self._author = author
        self._year = year
        self._is_borrowed = False
        self._borrow_date = None
        self._borrow_period_days = 14

    def get_title(self):
        # получить название книги
        return self._title

    def set_title(self, new_title):
        # поставить название книги
        self._title = new_title

    def get_author(self):
        # получить автора
        return self._author

    def set_author(self, author):
        # назначить/поставить автора
        self._author = author

    def change_author(self, new_author):
        # сменить автора
        self._author = new_author

    def get_year(self):
        # получить год книги
        return self._year

    def set_year(self, year):
        # выставить год книге
        self._year = year

    def get_info(self):
        # получить инфо о книге
        status = "на руках" if self._is_borrowed else "доступна"
        return (
            f"\n"
            f"информация о книжке\n"
            f"{'─' * 10}\n"
            f"название:  {self._title}\n"
            f"автор(ы):  {self._author}\n"
            f"год:       {self._year}\n"
            f"статус:    {status}\n"
            f"{'─' * 10}\n"
        )

    def get_age(self, current_year):
        # считает сколько лет книге
        return current_year - self._year

    def borrow_book(self):
        if self._is_borrowed:
            # если уже взята то пишем об этом
            print(f"книга \"{self._title}\" уже взята")
        else:
            self._is_borrowed = True
            self._borrow_date = datetime.now()
            print(f"книга \"{self._title}\" успешно взята")

    def return_book(self):
        if not self._is_borrowed:
            # если вдруг вернули книгу которую не брали
            print(f"книга \"{self._title}\" не была взята")
        else:
            self._is_borrowed = False
            self._borrow_date = None
            print(f"книга \"{self._title}\" возвращена")

    def is_borrowed(self):
        # возвращает статус
        return self._is_borrowed

    def extend_borrow_period(self, days):
        # продлевает срок на нужное количествр дней
        self._borrow_period_days += days



class EBook(Book):
    """
    Класс EBook, наследник Book, с дополнительными свойствами и
    методами

    Свойства:
        _download_link - ссылка для скачивания
        _format - формат файла

    Методы:
        get_format() / set_format() - получить/изменить формат
        change_format() - изменить формат
        get_download_link() / set_download_link() - получить/изменить ссылку
        update_download_link() - обновить ссылку
        send_download_link() - имитация отправки

    Аргументы:
        Книжка: книга
    """

    def __init__(self, title, author, year, download_link, file_format):
        """
        Аргументы:
            title (str): название книги
            author (str): автор книги
            year (int): год издания
            download_link (str): ссылка для скачивания
            file_format (str): формат файла
        """
        super().__init__(title, author, year)
        self._download_link = download_link
        self._format = file_format

    def get_format(self):
        # ретурним формат
        return self._format

    def set_format(self, new_format):
        # устанавливаем формат
        self._format = new_format

    def change_format(self, new_format):
        # меняем формат
        self._format = new_format

    def get_download_link(self):
        # отдаем ссылку
        return self._download_link

    def set_download_link(self, link):
        # устанавливаем ссылку
        self._download_link = link

    def update_download_link(self, new_link):
        # обновляем ссылку на нью ссылку
        self._download_link = new_link

    def send_download_link(self, email):
        # имитация отправки ссылки на почту
        print(f"ссылка отправлена на {email}: {self._download_link}")
