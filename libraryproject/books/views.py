from django.urls import reverse
from datetime import date
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from books.models import Book, Author, Genre


# Create your views here.

def index(request):
    books_list = Book.objects.all()
    context = {
        'books_list': books_list
    }
    return render(request, "books/index.html", context)

def details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "books/details.html", {'book': book})

def authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, "books/authors.html", context)

def authors_details(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books_list = author.books.all()
    return render(request, "books/authors_details.html", {'author': author, 'books_list': books_list})

def add_author(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birth_date = request.POST['birth_date']
        Author.objects.create(first_name=first_name, last_name=last_name, birth_date=birth_date)
        return HttpResponseRedirect(reverse("books:authors"))
    return render(request, "books/add_authors.html")

def genres(request):
    genres = Genre.objects.all()
    lista_genero_libros = []

    for genre in genres:
        numbooks = genre.books_genre.count()
        lista_genero_libros.append((genre, numbooks))

    context = {
        'lista_genero_libros': lista_genero_libros,
    }
    return render(request, "books/genres.html", context)


def genres_details(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    books_list = genre.books_genre.all()
    context = {
        'genre': genre,
        'books_list': books_list
    }
    return render(request, "books/genres_details.html",context)

def add_book(request):

    authors_list = Author.objects.all()
    genre_list = Genre.objects.all()

    if request.method == "POST":

        title = request.POST.get('title')
        author_id = request.POST.get('author')
        genre_id = request.POST.get('genre')
        published_date = request.POST.get('published_date')
        summary = request.POST.get('summary')

        author = get_object_or_404(Author, pk=author_id)
        genre = get_object_or_404(Genre, pk=genre_id)

        book = Book.objects.create(title=title,genre=genre,publish_date=published_date,summary=summary)
        book.author.add(author)
        return HttpResponseRedirect(reverse("books:index"))

    context = {
        'authors_list': authors_list,
        'genre_list': genre_list,
    }
    return render(request, "books/add_books.html", context)

def recent_books(request):
    hoy = date.today()
    hace_5_años = date(hoy.year - 5, hoy.month, hoy.day)

    # Filtra los libros publicados después de esa fecha
    recent_books_list = Book.objects.filter(publish_date__gte=hace_5_años)

    context = {
        'recent_books_list': recent_books_list,
    }
    return render(request, "books/recent_books.html", context)
