from django.shortcuts import render

def blog(request):
    return render(request, 'blog/index.html', locals())

# Create your views here.
