from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages  #for flash messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):

    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for { username } !!')
            return redirect('login')
    else:
        form= UserRegisterForm()

    context = {'form': form , 'title': 'Register-Blog'}
    return render(request, 'users/register.html' , context)

@login_required
def profile(request):
    context = {'title': 'Register-Blog'}
    return render(request, 'users/profile.html' , context)