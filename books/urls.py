
from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.show_all_books, name = 'index'),
    path('<int:id>/', views.return_books_by_id, name='book_details'),
    path('add_book/', views.add_book, name = 'add_book'),
    path('<int:id>/update_book/', views.update_book, name = 'update_book'),  
     path('<int:id>/delete_book/', views.delete_book, name = 'delete_book'),  

]
