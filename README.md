# qa_python
Добавил тесты:
`test_add_new_book_incorrect_len_name_not_added` - [параметризованный] проверяет, что книга с некорректной длинной не создается
`test_add_new_book_duplicate_names_not_added` - проверяет, что не создаются дубли
`test_set_book_genre_correct_data_added` - [параметризованный] проверка корректного добавления жанров для книги
`test_set_book_genre_name_not_in_list_not_added` - проверка добавления жанра для книги, когда жанр не из списка
`test_get_book_genre_correct_data_return` - проверка корректного отображения жанра
`test_get_books_with_specific_genre_correct_data_return` - проверка корректной фильтрации по жанру
`test_get_books_genre_correct_data_return` - проверка отображения словаря книг
`test_get_books_for_children_correct_data_return` - [параметризованный] проверка фильтрации жанров для детей
`test_add_book_in_favorites_books_correct_data_added` - проверка отображения списка "favorites" после изменений