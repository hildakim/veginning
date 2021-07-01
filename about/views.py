from django.shortcuts import render

# Create your views here.

def about_view(request):
    return render(request, 'forstarter.html')

def why_view(request):
    return render(request, 'why.html')

def more_view(request):
    return render(request, 'more.html')

def bad_view(request):
    return render(request, 'bad.html')
