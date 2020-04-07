from django.shortcuts import render
from django.http import HttpResponse
from .models import post


# Create your views here.
def index(request):
    context={
        'posts': post.objects.order_by('id'),
        'title':'lol'
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'lol2'})