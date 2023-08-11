from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language
from django.views import generic
# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_fantasy_books = Book.objects.filter(genre__name__icontains='fantasy').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_fantasy_books': num_fantasy_books,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book


# BookDetailView class as a view function instead \/
# def book_detail_view(request, primary_key):
#     try:
#         book = Book.objects.get(pk=primary_key)
#     except Book.DoesNotExist:
#         raise Http404('Book does not exist')

#     return render(request, 'catalog/book_detail.html', context={'book': book})

# The same view function for BookDetailView as above but with the shortcut function \/

# from django.shortcuts import get_object_or_404

# def book_detail_view(request, primary_key):
#     book = get_object_or_404(Book, pk=primary_key)
#     return render(request, 'catalog/book_detail.html', context={'book': book})


# You can add attributes to change the default behavior above. For example, you can
# specify another template file if you need to have multiple views that use this same
# model, or you might want to use a different template variable name if book_list is not
# intuitive for your particular template use-case. Possibly the most useful variation is
# to change/filter the subset of results that are returned — so instead of listing all
# books you might list top 5 books that were read by other users.

# class BookListView(generic.ListView):
#     model = Book
#     context_object_name = 'book_list'   # your own name for the list as a template variable
#     queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
#     template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

#  ^FOR AI INTEGRATION LATER^


# Override "get_conteect_data()" method in class
# class BookListView(generic.ListView):
#     model = Book

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get the context
#         context = super(BookListView, self).get_context_data(**kwargs)
#         # Create any data and add it to the context
#         context['some_data'] = 'This is just some data'
#         return context
# When doing this it is important to follow the pattern used above:

# First get the existing context from our superclass.
# Then add your new context information.
# Then return the new (updated) context.
