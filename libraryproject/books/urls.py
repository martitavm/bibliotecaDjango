from django.urls import path

from books import views

app_name = "books"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:book_id>/", views.details, name="details"),
    path("authors/", views.authors, name="authors"),
    path("authors/<int:author_id>/", views.authors_details, name="authors_details"),
    path("authors/add_author/", views.add_author, name="add_author"),
    path("genres/", views.genres, name="genres"),
    path("genres/<int:genre_id>/", views.genres_details, name="genres_details"),
    path("add_book/", views.add_book, name="add_book"),
    path("recent_books/", views.recent_books, name="recent_books"),
]