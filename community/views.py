from django.shortcuts import render

# Create your views here.
def free_view(request):
    return render(request, 'commuIndex.html')

def recipe_view(request):
    return render(request, 'recipe.html')

def restaurant_view(request):
    return render(request, 'restaurant.html')