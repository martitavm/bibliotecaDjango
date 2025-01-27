from http.client import responses
from django.test import TestCase
from django.urls import reverse
from books.models import Author, Book, Genre


class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="John", last_name="Doe", birth_date="1970-01-01")

    def test_author_creation(self):
        self.assertEqual(self.author.first_name, "John")
        self.assertEqual(self.author.last_name, "Doe")
        self.assertEqual(str(self.author), "John Doe")  # Asume que el método __str__ está implementado.


class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="John", last_name="Doe", birth_date="1970-01-01")
        self.book = Book.objects.create(
            title="Sample Book",
            genre=Genre.objects.create(name="Fiction"),
            publish_date="2020-01-01",
            summary="A sample book for testing purposes."
        )
        self.book.author.add(self.author)

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Sample Book")
        self.assertIn(self.author, self.book.author.all())
        self.assertEqual(self.book.genre.name, "Fiction")


class ViewTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="John", last_name="Doe", birth_date="1970-01-01")
        self.genre = Genre.objects.create(name="Fiction")
        self.book = Book.objects.create(
            title="Sample Book",
            genre=self.genre,
            publish_date="2020-01-01",
            summary="A sample book for testing purposes."
        )
        self.book.author.add(self.author)

    def test_book_list_view(self):
        response = self.client.get(reverse("books:index"))  # Asume que la URL está nombrada.
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Book")

    def test_author_list_view(self):
        response = self.client.get(reverse("books:authors"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")

    def test_genre_list_view(self):
        response = self.client.get(reverse("books:genres"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fiction")

    def test_book_detail_view(self):
        response = self.client.get(reverse("books:details", args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Book")
        self.assertContains(response, "John Doe")

    def test_author_detail_view(self):
        response = self.client.get(reverse("books:authors_details", args=[self.author.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John")
        self.assertContains(response, "Doe")

    def test_genre_detail_view(self):
        response = self.client.get(reverse("books:genres_details", args=[self.genre.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fiction")

    def test_authors_add_view(self):
        response = self.client.get(reverse("books:add_author"))
        self.assertEqual(response.status_code, 200)

    def test_books_add_view(self):
        response = self.client.get(reverse("books:add_book"))
        self.assertEqual(response.status_code, 200)

    def test_recent_books_view(self):
        response = self.client.get(reverse("books:recent_books"))
        self.assertEqual(response.status_code, 200)
