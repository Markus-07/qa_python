import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()


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


def test_add_new_book_count_change(collector):
    before_count = len(collector.books_genre)
    collector.add_new_book("Новая книга")
    after_count = len(collector.books_genre)
    assert after_count - before_count == 1


def test_add_new_book_adds_to_dict(collector):
    name = "Уникальная книга"
    collector.add_new_book(name)
    assert collector.books_genre.get(name) == ""


def test_add_new_book_duplicate_count_unchanged(collector):
    name = "Дубликат"
    collector.add_new_book(name)
    collector.add_new_book(name)
    assert len(collector.books_genre) == 1


def test_add_new_book_duplicate_book_exists(collector):
    name = "Дубликат"
    collector.add_new_book(name)
    collector.add_new_book(name)
    assert name in collector.books_genre


def test_set_book_genre_valid(collector):
    name = "Фантастическая книга"
    genre = "Фантастика"
    collector.add_new_book(name)
    collector.set_book_genre(name, genre)
    assert collector.get_book_genre(name) == genre


def test_set_book_genre_book_not_exists(collector):
    name = "Неизвестная книга"
    genre = "Детективы"
    collector.set_book_genre(name, genre)
    assert collector.get_book_genre(name) is None


def test_get_books_for_children_includes_valid_book(collector):
    collector.add_new_book("Детская сказка")
    collector.set_book_genre("Детская сказка", "Комедии")
    assert "Детская сказка" in collector.get_books_for_children()


def test_get_books_for_children_excludes_invalid_book(collector):
    collector.add_new_book("Страшный детектив")
    collector.set_book_genre("Страшный детектив", "Детективы")
    assert "Страшный детектив" not in collector.get_books_for_children()


def test_add_book_in_favorites_valid(collector):
    name = "Любимая книга"
    collector.add_new_book(name)
    collector.add_book_in_favorites(name)
    assert name in collector.get_list_of_favorites_books()


def test_add_book_in_favorites_book_not_exists(collector):
    name = "Ещё не добавлена"
    collector.add_book_in_favorites(name)
    assert name not in collector.get_list_of_favorites_books()


def test_add_book_in_favorites_adds_book(collector):
    name = "Для удаления"
    collector.add_new_book(name)
    collector.add_book_in_favorites(name)
    assert name in collector.get_list_of_favorites_books()


def test_delete_book_from_favorites_removes_book(collector):
    name = "Для удаления"
    collector.add_new_book(name)
    collector.add_book_in_favorites(name)
    collector.delete_book_from_favorites(name)
    assert name not in collector.get_list_of_favorites_books()


def test_get_books_genre_returns_correct_genre(collector):
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")

    result = collector.get_books_genre()

    assert isinstance(result, dict), "Метод должен возвращать словарь"
    assert "Гарри Поттер" in result, "Книга должна быть в словаре"
    assert result["Гарри Поттер"] == "Фантастика", "Жанр должен совпадать с установленным"
