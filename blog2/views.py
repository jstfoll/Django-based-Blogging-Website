from django.shortcuts import render

# Create your views here.
def about2(request):
    return render(request, 'blog2/home.html',{'title':'lol2'})