class BookData:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return ",".join(self.books)


class TestBookDataDecorator:
    def test_unDecoratedFunction(self):
        self.books = BookData("Harry Potter", "To Kill a Mockingbird", "The 1818 Text: Frankenstein")
        assert "Harry Potter,To Kill a Mockingbird,The 1818 Text: Frankenstein" == str(self.books)
