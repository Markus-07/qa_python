import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


# 1. add_new_book: добавление книг с разной длиной названия (параметризованный)
@pytest.mark.parametrize("name,expected_added", [
    ("Книга1", True),
    ("A" * 40, True),
    ("", False),
    ("A" * 41, False),
])
def test_add_new_book(collector, name, expected_added):
    before_count = len(collector.books_genre)
    collector.add_new_book(name)
    after_count = len(collector.books_genre)

    assert (after_count - before_count == 1) == expected_added
    if expected_added:
        assert collector.books_genre.get(name) == ""


# 2. add_new_book: нельзя добавить одну и ту же книгу дважды
def test_add_new_book_duplicate(collector):
    name = "Дубликат"
    collector.add_new_book(name)
    collector.add_new_book(name)
    assert len(collector.books_genre) == 1
    assert name in collector.books_genre


# 3. set_book_genre: успешная установка жанра
def test_set_book_genre_valid(collector):
    name = "Фантастическая книга"
    genre = "Фантастика"
    collector.add_new_book(name)
    collector.set_book_genre(name, genre)
    assert collector.get_book_genre(name) == genre


# 4. set_book_genre: книга не существует в словаре
def test_set_book_genre_book_not_exists(collector):
    name = "Неизвестная книга"
    genre = "Детективы"
    collector.set_book_genre(name, genre)
    assert collector.get_book_genre(name) is None


# 5. set_book_genre: жанр не из списка genre
def test_set_book_genre_invalid_genre(collector):
    name = "Книга без жанра"
    invalid_genre = "Фэнтези"
    collector.add_new_book(name)
    collector.set_book_genre(name, invalid_genre)
    assert collector.get_book_genre(name) != invalid_genre


# 6. get_books_with_specific_genre: фильтрация по жанру (параметризованный)
@pytest.mark.parametrize("genre,expected_books", [
    ("Фантастика", ["Книга1", "Книга2"]),
    ("Ужасы", []),
])
def test_get_books_with_specific_genre(collector, genre, expected_books):
    collector.add_new_book("Книга1")
    collector.add_new_book("Книга2")
    collector.set_book_genre("Книга1", "Фантастика")
    collector.set_book_genre("Книга2", "Фантастика")

    result = collector.get_books_with_specific_genre(genre)
    assert sorted(result) == sorted(expected_books)


# 7. get_books_for_children: книги без возрастного рейтинга
def test_get_books_for_children(collector):
    collector.add_new_book("Детская сказка")
    collector.add_new_book("Страшный детектив")
    collector.set_book_genre("Детская сказка", "Комедии")
    collector.set_book_genre("Страшный детектив", "Детективы")

    children_books = collector.get_books_for_children()
    assert "Детская сказка" in children_books
    assert "Страшный детектив" not in children_books


# 8. add_book_in_favorites: добавление книги, которая есть в books_genre
def test_add_book_in_favorites_valid(collector):
    name = "Любимая книга"
    collector.add_new_book(name)
    collector.add_book_in_favorites(name)
    assert name in collector.get_list_of_favorites_books()


# 9. add_book_in_favorites: книга не в books_genre
def test_add_book_in_favorites_book_not_exists(collector):
    name = "Ещё не добавлена"
    collector.add_book_in_favorites(name)
    assert name not in collector.get_list_of_favorites_books()


# 10. delete_book_from_favorites и get_list_of_favorites_books
def test_delete_book_from_favorites(collector):
    name = "Для удаления"
    collector.add_new_book(name)
    collector.add_book_in_favorites(name)
    assert name in collector.get_list_of_favorites_books()

    collector.delete_book_from_favorites(name)
    assert name not in collector.get_list_of_favorites_books()
