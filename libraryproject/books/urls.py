from django.urls import path

from books import views

app_name = "books"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:book_id>/", views.details, name="details"),
    path("authors/", views.authors, name="authors"),
    path("authors/<int:author_id>/", views.authors_details, name="authors_details"),
    path("authors/add_author/", views.add_author, name="add_author"),
    path("authors/add_authors/", views.add_authors, name="add_authors"),
]