# qa_python

Проект для тестирования функционала работы с книгами.

## Стек
- Python
- pytest

## Функционал
- Добавление новых книг
- Установка жанра для книги
- Поиск книг по жанру
- Управление списком избранного (добавление/удаление)

## Покрытые тестами сценарии
- Проверка изменения количества книг при добавлении (`test_add_new_book_count_change`)
- Проверка добавления книги в словарь (`test_add_new_book_adds_to_dict`)
- Проверка запрета на дублирование книг: количество не меняется (`test_add_new_book_duplicate_count_unchanged`)
- Проверка запрета на дублирование книг: книга существует (`test_add_new_book_duplicate_book_exists`)
- Проверка успешной установки жанра (`test_set_book_genre_valid`)
- Проверка обработки несуществующей книги при установке жанра (`test_set_book_genre_book_not_exists`)
- Проверка фильтрации книг по жанру (`test_get_books_with_specific_genre`)
- Проверка получения детских книг: валидная книга включена (`test_get_books_for_children_includes_valid_book`)
- Проверка получения детских книг: невалидная книга исключена (`test_get_books_for_children_excludes_invalid_book`)
- Проверка добавления книги в избранное (`test_add_book_in_favorites_valid`)
- Проверка отказа в добавлении несуществующей книги в избранное (`test_add_book_in_favorites_book_not_exists`)
- Проверка добавления книги в избранное (для теста удаления) (`test_add_book_in_favorites_adds_book`)
- Проверка удаления книги из избранного (`test_delete_book_from_favorites_removes_book`)
- Проверка получения словаря книг (`test_get_books_genre_returns_correct_genre`): метод `get_books_genre()` возвращает полный словарь всех книг с их жанрами. Тест добавляет книгу, присваивает ей допустимый жанр и проверяет, что словарь содержит книгу с корректным значением жанра.

## Запуск тестов
```bash
python -m pytest -v tests.py
