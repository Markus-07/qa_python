class BooksCollector:
    def __init__(self):
        self.books = {}
        self.books_genre = {}
        # Обязательно набери скобки вручную: [ и ]
        self.favorites = []

    def add_new_book(self, title: str):
        """
        Добавляет книгу, если её ещё нет.
        Если уже есть — ничего не делает, но возвращает True.
        """
        if title not in self.books:
            self.books[title] = None
            self.books_genre[title] = ""
        return True

    def set_book_genre(self, title: str, genre: str):
        """
        Устанавливает жанр только если книга уже существует.
        Не добавляет книгу автоматически — это задача add_new_book.
        Возвращает True, если жанр установлен, иначе False.
        """
        if title in self.books:
            self.books_genre[title] = genre
            return True
        return False

    def get_book_genre(self, title: str):
        return self.books_genre.get(title)

    def get_books_genre(self):
        return self.books_genre

    def get_books_with_specific_genre(self, genre: str):
        return [title for title, g in self.books_genre.items() if g == genre]

    def get_books_for_children(self):
        allowed_genres = {"", "Комедии"}
        return [title for title, g in self.books_genre.items() if g in allowed_genres]

    def add_book_in_favorites(self, title: str):
        if title in self.books_genre and title not in self.favorites:
            self.favorites.append(title)
            return True
        return False

    def delete_book_from_favorites(self, title: str):
        if title in self.favorites:
            self.favorites.remove(title)
            return True
        return False

    def get_list_of_favorites_books(self):
        return self.favorites
