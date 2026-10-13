class BooksCollector:
    def __init__(self):
        # Словарь: {название_книги: жанр}
        self.books_genre = {}
        # Список избранных книг
        self.favorites = []
        # Допустимые жанры
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        # Жанры с возрастными ограничениями
        self.genre_age_rating = ['Ужасы', 'Детективы']

    def add_new_book(self, name: str) -> bool:
        """Добавляет книгу, если имя не пустое и не длиннее 40 символов."""
        if not name or len(name) > 40:
            return False
        
        if name not in self.books_genre:
            self.books_genre[name] = ""  # Жанр пока пустой
            return True
        return False

    def set_book_genre(self, name: str, genre: str) -> None:
        """Устанавливает жанр для книги, если она существует и жанр разрешён."""
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    def get_book_genre(self, name: str):
        """Возвращает жанр книги по её названию."""
        return self.books_genre.get(name)

    def get_books_with_specific_genre(self, genre: str) -> list[str]:
        """Возвращает список книг заданного жанра."""
        return [book for book, g in self.books_genre.items() if g == genre]

    def get_books_for_children(self) -> list[str]:
        """
        Возвращает книги, подходящие детям.
        Логика: книга подходит, если её жанр есть в списке допустимых
        и при этом не входит в список жанров с возрастными ограничениями.
        """
        return [
            book for book, genre in self.books_genre.items()
            if genre in self.genre and genre not in self.genre_age_rating
        ]

    def add_book_in_favorites(self, name: str) -> None:
        """Добавляет книгу в избранное, только если она есть в коллекции и ещё не в избранном."""
        if name in self.books_genre and name not in self.favorites:
            self.favorites.append(name)

    def delete_book_from_favorites(self, name: str) -> None:
        """Удаляет книгу из избранного, если она там есть."""
        if name in self.favorites:
            self.favorites.remove(name)

    def get_list_of_favorites_books(self) -> list[str]:
        """Возвращает список избранных книг."""
        return self.favorites

