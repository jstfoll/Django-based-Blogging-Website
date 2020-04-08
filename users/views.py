from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages  #for flash messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):

    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for { username } !!')
            return redirect('home')
    else:
        form= UserRegisterForm()

    context = {'forms': form }
    return render(request, 'users/register.html' , context)
