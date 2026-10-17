from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# from django.views.decorators.cache import cache_page



# Create your views here.
@login_required
# @cache_page(60 * 10)
def show_all_books(request):

    books = Book.objects.all()

    paginator = Paginator(books,4)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)


    context = {

         'page_obj' : page_obj
    }

    return render(request, 'books/index.html', context)

@login_required
def return_books_by_id(request, id):

    book = get_object_or_404(Book, id=id)

    context = {
    
             'book' : book
        }

    return render(request, 'books/book_detail.html', context)

@login_required
def add_book(request):

   if request.method == "POST":
      form = BookForm(request.POST)

      if form.is_valid():
        book = form.save(commit=False)
        book.added_by = request.user
        book.status = book.status.capitalize()
        book.save()
        messages.success(request, 'your book is added Successfuly')
        return redirect('books:index')
    
   else:

       form = BookForm()

   context = {
     'form' : form,
  }

   return render(request, 'books/add_book.html', context)

@login_required
def update_book(request,id):

   book = get_object_or_404(Book, id=id)
   if book.added_by == request.user:

      
      if request.method== 'POST':
         form = BookForm(request.POST,instance=book)


         if form.is_valid():
            book = form.save(commit=False)
            book.status = book.status.capitalize()
            book.save()
            return redirect('books:book_details', id=id)

      else:
         
         form = BookForm(instance=book)

   context = {

      'form': form,
      'book':book
   }

   return render(request, 'books/add_book.html', context)

@login_required
def delete_book(request,id):

   book = get_object_or_404(Book, id=id)
   if book.added_by == request.user:
      if request.method == 'POST':
         book.delete()
         return redirect('books:index')

   context= {
      'book': book
   }
      
   return render(request, 'books/delete_book.html',context)

