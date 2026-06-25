from library.book_module import Book, EBook
print("Тестинг/имитация работы classа Book...")

print()

book = Book("TCP/IP. Архитектура. Протоколы. Реализация. 2-е издание", "Фейт Сидни", 2022)

book.set_title("Алгоритмы и структуры данных для тех, кто ненавидит читать лонгриды")
book.set_author("Исида Моритэру, Миядзаки Сюити")
book.set_year(2026)

book.borrow_book()
book.return_book()

book.extend_borrow_period(7)

print(book.get_info())
print(f"возраст книги: {book.get_age(2026)} лет")

print()

print("Тестинг/имитация работы classа EBook...")

print()

ebook = EBook("Компьютерные сети. 6-е издание.", "Таненбаум Эндрю С., Фимстер Ник, Уэзеролл Дэвид", 2023, "https://books.kvantorim69.ru/books/computer-networks_book.pdf", "PDF")

# хорошее задание, познал про формат EPUB. и еще спасибо хабру :)

ebook.set_format("EPUB")
ebook.set_download_link("https://books.kvantorim69.ru/books/computer-networks_book.epub")

ebook.send_download_link("lovelisa228@mail.ru")

print(ebook.get_info())
print(f"формат: {ebook.get_format()}")
print(f"ссылка: {ebook.get_download_link()}")
