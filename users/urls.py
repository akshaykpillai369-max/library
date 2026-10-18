from django.urls import path
from . import views
from django.contrib.auth import views as login_view


app_name = 'users'

urlpatterns = [

     path('sign_up/', views.sign_up, name = 'sign_up'),
     path('login/', login_view.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
     path('logout/', views.logout, name='logout'),
     path('profile/',views.profile, name='profile'),

]


