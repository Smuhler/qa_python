import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('name', ['', 'Lorem ipsum dolor sit amet, consectetuer '])
    def test_add_new_book_incorrect_len_name_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    def test_add_new_book_duplicate_names_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Harry Potter and python')
        collector.add_new_book('Harry Potter and python')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('name, genre', [['Фантастика', 'Фантастика'], ['Ужас', 'Ужасы'], ['Детектив', 'Детективы'],
                                             ['Мультфильм', 'Мультфильмы'], ['Комедия', 'Комедии']])
    def test_set_book_genre_correct_data_added(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_name_not_in_list_not_added(self):
        collector = BooksCollector()
        collector.set_book_genre('Harry Potter and python', 'Ужасы')
        assert collector.get_books_genre() == {}

    def test_get_book_genre_correct_data_return(self):
        collector = BooksCollector()
        collector.add_new_book('Harry Potter and python')
        collector.set_book_genre('Harry Potter and python', 'Ужасы')
        assert collector.get_book_genre('Harry Potter and python') == 'Ужасы'

    def test_get_books_with_specific_genre_correct_data_return(self):
        collector = BooksCollector()
        collector.add_new_book('Harry Potter and python')
        collector.add_new_book('Harry Potter2 and python')
        collector.add_new_book('Harry Potter3 and python')
        collector.set_book_genre('Harry Potter and python', 'Ужасы')
        collector.set_book_genre('Harry Potter2 and python', 'Мультфильмы')
        collector.set_book_genre('Harry Potter3 and python', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Harry Potter and python',
                                                                    'Harry Potter3 and python']

    def test_get_books_genre_correct_data_return(self):
        collector = BooksCollector()
        collector.add_new_book('Harry Potter and python')
        collector.add_new_book('Harry Potter2 and python')
        collector.set_book_genre('Harry Potter and python', 'Ужасы')
        assert collector.get_books_genre() == {'Harry Potter and python': 'Ужасы', 'Harry Potter2 and python': ''}

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_correct_data_return(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Harry Potter and python')
        collector.add_new_book('Harry Potter2 and python')
        collector.add_new_book('Harry Potter3 and python')
        collector.set_book_genre('Harry Potter and python', genre)
        collector.set_book_genre('Harry Potter2 and python', 'Мультфильмы')
        collector.set_book_genre('Harry Potter3 and python', genre)
        assert collector.get_books_for_children() == ['Harry Potter2 and python']


    def test_add_book_in_favorites_books_correct_data_added(self):
        collector = BooksCollector()
        collector.add_new_book('Harry Potter and python')
        collector.add_new_book('Harry Potter2 and python')
        collector.add_book_in_favorites('Harry Potter and python')
        collector.add_book_in_favorites('Harry Potter2 and python')
        collector.delete_book_from_favorites('Harry Potter and python')
        assert collector.get_list_of_favorites_books() == ['Harry Potter2 and python']

