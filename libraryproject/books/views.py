from django.urls import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from books.models import Book, Author


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

def add_authors(request):
    return render(request, "books/add_authors.html")