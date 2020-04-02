from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author':'Pratik Bharuka',
        'title':'blog post 1',
        'content':'first post content',
        'date':'1 April,2019'

    },
    {
        'author':'Harsha Bharuka',
        'title':'blog post 2',
        'content':'second post content',
        'date':'2 April,2019'

    },
]

# Create your views here.
def index(request):
    context={
        'posts': posts,
        'title':'lol'
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'lol2'})

def about2(request):
    return render(request, 'blog/about2.html',{'title':'lol3'})