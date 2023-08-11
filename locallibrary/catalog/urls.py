from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]

# For Django class-based views we access an appropriate view function by calling the
# class method as_view(). This does all the work of creating an instance of the class,
# and making sure that the right handler methods are called for incoming HTTP requests.
