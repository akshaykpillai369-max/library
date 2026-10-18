from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages 
from .forms import SignUpForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from . models import User

# Create your views here.
def sign_up(request):

    if request.method == "POST":

        form = SignUpForm(request.POST)

        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hello {username}, your account is created Successfuly, Now Login with that credientials')
            return redirect('users:login')

    else:

        form = SignUpForm()

    context = {
        'form': form
    }

    return render(request, 'users/sign_up.html', context)

def logout(request):

    auth_logout(request)

    messages.success(request,'You Logged out Successfully')
    return redirect('users:login')

@login_required
def profile(request):
   
   context = {
       
       'profile_user' : request.user
   }

   return render(request, 'users/profile.html',context)

    
