from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .forms import ProductForm
from .models import Product



def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def book(request):
    return render(request, 'book.html')

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'index.html', {'form': form})