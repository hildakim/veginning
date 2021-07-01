from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Store
from .models import Store2
from .forms import StoreForm
from .forms import StoreForm2
from .models import Store3
from .forms import StoreForm3

def product(request):
    pmain = Store.objects
    p_list = Store.objects.all()
    paginator = Paginator(p_list, 10)
    p_page = request.GET.get('p_page')
    p_posts = paginator.get_page(p_page)
    return render(request, 'product.html', {'pmain': pmain, 'p_posts': p_posts})

def productsub(request, id):
    psub = get_object_or_404(Store, pk = id)
    return render(request, 'productsub.html', {'psub': psub})

def cosmetics(request):
    cmain = Store2.objects
    c_list = Store2.objects.all()
    paginator = Paginator(c_list, 10)
    c_page = request.GET.get('c_page')
    c_posts = paginator.get_page(c_page)
    return render(request, 'cosmetics.html', {'cmain': cmain, 'c_posts': c_posts})

def cosmeticssub(request, id):
    csub = get_object_or_404(Store2, pk = id)
    return render(request, 'cosmeticssub.html', {'csub': csub})

def household(request):
    hmain = Store3.objects
    h_list = Store3.objects.all()
    paginator = Paginator(h_list, 10)
    h_page = request.GET.get('h_page')
    h_posts = paginator.get_page(h_page)
    return render(request, 'household.html', {'hmain': hmain, 'h_posts': h_posts})

def householdsub(request, id):
    hsub = get_object_or_404(Store3, pk = id)
    return render(request, 'householdsub.html', {'hsub': hsub})

def productnew(request):
    if request.method =='POST':
        new_form = StoreForm3(request.POST, request.FILES)
        if new_form.is_valid():
            new_create = new_form.save(commit = False)
            new_create.pub_date = timezone.now()
            new_create.save()
            return redirect('household')
    else:
        new_form = StoreForm()
        return render(request, 'productnew.html', {'new_form':new_form})

def productedit(request, id):
    pedit= get_object_or_404(Store3, pk = id)
    if request.method == 'GET':
        p_form = StoreForm3(instance = pedit)
        return render(request, 'productedit.html', {'p_edit':p_form})
    else:
        p_form = StoreForm3(request.POST, request.FILES, instance = pedit)
        if p_form.is_valid():
            pedit = p_form.save(commit = False)
            pedit.pub_date = timezone.now()
            pedit.save()
        return redirect('household')

def productdelete(request, id):
    pdelete = Store.objects.get(id = id)
    pdelete.delete()
    return redirect('product')


