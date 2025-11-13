from django.shortcuts import render , redirect
from app.forms import BookForm
from app.models import Book
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book Create Successfully!')
            return redirect('book_create')
    else:
        form = BookForm
        
    return render(request,'app/book_form.html',{'form':form})
# book_ List:

def book_list(request):
    # Base query — latest books first
    books = Book.objects.all().order_by('-created_at')
    
    
 # Get query parameters from search form
    query = request.GET.get('q')
    genre = request.GET.get('genre')
    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

 # Filter by genre
    if genre:
        books = books.filter(genre=genre)

    context = {
        'books': books,
        'query': query,
        'genre': genre,
    }

    return render(request, 'app/book_list.html', context)

# book deatils

def book_details(request,pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'app/book_details.html',{'book':book})


#  book upadte 

def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book update successfully!!')
            return redirect('book-update', pk=book.pk)
    
    else:
        form = BookForm(instance=book)
        return render(request, 'app/book_form.html',{'form':form})
    
    
    # book delete.
    
    
def book_delete(request,pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    messages.success(request, 'Book delete successfully!!')
    return redirect('book-list')
    
