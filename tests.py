import pytest

from main import BooksCollector

class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    @pytest.mark.parametrize('name', ['Cобака на сене', 'Старик и море'])
    def test_add_new_book_two_books(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.books_genre

    def test_add_new_book_with_long_name(self, collector):
        collector.add_new_book('очень длинное название книги которое больше, чем сорок символов')
        assert len(collector.books_genre) == 0

    def test_set_book_genre_one_book(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец','Фантастика')
        assert collector.books_genre['Властелин колец'] == 'Фантастика'

    @pytest.mark.parametrize('name,genre', [['Горе от ума','Комедии'], ['Трое в лодке не считая собаки','Комедии']])
    def test_get_book_genre_two_books(self, collector, name, genre):
        collector.add_new_book('Горе от ума')
        collector.add_new_book('Трое в лодке не считая собаки')
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == 'Комедии' and len(collector.books_genre) == 2

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        specific_genre = collector.get_books_with_specific_genre('Фантастика')
        assert specific_genre[0] == 'Властелин колец'

    def test_get_books_genre(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert collector.get_books_genre() == {'Властелин колец': 'Фантастика'}

    @pytest.mark.parametrize('name,genre', [['Ну погоди!!!', 'Мультфильмы'], ['Ежик в тумане', 'Ужасы']])
    def test_get_books_for_children(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        kids = collector.get_books_for_children()
        for item in kids:
            assert not item == 'Ежик в тумане' and len(kids) == 1

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        assert 'Властелин колец' in collector.favorites

    def test_delete_book_from_favorites(self, collector):
        book = 'Оно'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert book not in collector.favorites

    def test_get_list_of_favorites_books_two_books(self, collector):
        collector.add_new_book('Скотный двор')
        collector.add_new_book('Бойцовский клуб')
        collector.add_book_in_favorites('Скотный двор')
        collector.add_book_in_favorites('Бойцовский клуб')
        favorite_books = collector.get_list_of_favorites_books()
        assert favorite_books == ['Скотный двор', 'Бойцовский клуб'] and len(favorite_books) == 2
