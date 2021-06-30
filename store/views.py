from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Store
from .forms import StoreForm

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

def productnew(request):
    if request.method =='POST':
        new_form = StoreForm(request.POST, request.FILES)
        if new_form.is_valid():
            new_create = new_form.save(commit = False)
            new_create.pub_date = timezone.now()
            new_create.save()
            return redirect('product')
    else:
        new_form = StoreForm()
        return render(request, 'productnew.html', {'new_form':new_form})
def productedit(request, id):
    pedit= get_object_or_404(Store, pk = id)
    if request.method == 'GET':
        p_form = StoreForm(instance = pedit)
        return render(request, 'productedit.html', {'p_edit':p_form})
    else:
        p_form = StoreForm(request.POST, request.FILES, instance = pedit)
        if p_form.is_valid():
            pedit = p_form.save(commit = False)
            pedit.pub_date = timezone.now()
            pedit.save()
        return redirect('product')

def productdelete(request, id):
    pdelete = Store.objects.get(id = id)
    pdelete.delete()
    return redirect('product')


