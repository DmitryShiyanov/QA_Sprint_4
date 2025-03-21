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
