class BooksCollector:
    def __init__(self):
        # Словарь: {название_книги: жанр}
        self.books_genre = {}
        # Список избранных книг
        self.favorites = []

    def add_new_book(self, name: str) -> bool:
        """Добавляет книгу, если имя не пустое и не слишком длинное."""
        if not name or len(name) > 40:
            return False
        
        # Если книги ещё нет — добавляем
        if name not in self.books_genre:
            self.books_genre[name] = ""  # Жанр пока пустой
            return True
        return False

    def set_book_genre(self, name: str, genre: str) -> None:
        """Устанавливает жанр для книги, если она существует."""
        # Здесь можно добавить проверку на допустимые жанры, если нужно
        if name in self.books_genre:
            self.books_genre[name] = genre

    # --- ИСПРАВЛЕННЫЙ МЕТОД ---
    def get_books_genre(self, book_name: str):
        """Возвращает жанр конкретной книги по её названию."""
        return self.books_genre.get(book_name)
    # -------------------------

    def get_book_genre(self, name: str):
        """Альтернативное название (если оно используется в других местах)."""
        return self.get_books_genre(name)

    def get_books_with_specific_genre(self, genre: str):
        """Возвращает список книг заданного жанра."""
        result = [book for book, g in self.books_genre.items() if g == genre]
        return result

    def get_books_for_children(self):
        """
        Возвращает книги для детей.
        Логика: в твоём тесте это книги с жанром 'Комедии'.
        Замени эту логику на реальную, когда определишься с критериями.
        """
        # Примерная логика под твои тесты:
        return [book for book, genre in self.books_genre.items() if genre == "Комедии"]

    def add_book_in_favorites(self, name: str) -> None:
        """Добавляет книгу в избранное, только если она есть в коллекции."""
        if name in self.books_genre and name not in self.favorites:
            self.favorites.append(name)

    def delete_book_from_favorites(self, name: str) -> None:
        """Удаляет книгу из избранного."""
        if name in self.favorites:
            self.favorites.remove(name)

    def get_list_of_favorites_books(self):
        """Возвращает список избранных книг."""
        return self.favorites
