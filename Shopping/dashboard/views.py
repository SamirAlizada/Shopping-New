from django.shortcuts import render, redirect
from .forms import CategoryForm, ProductForm
from mehsullar.models import Category, Product


def dashboard_index(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'products' : products,
        'categories' : categories
    }
    
    return render(request, 'dashboard_index.html', context)

def dash_products(request):
  products = Product.objects.all()

  context = {
    "products" : products,
  }

  return render(request, "dash_products.html", context)


def dash_categories(request):
  categories = Category.objects.all()

  context = {
    "categories" : categories,
  }

  return render(request, "dash_categories.html", context)

def dash_create_category(request):
  form = CategoryForm()
  if request.method == "POST":
    form = CategoryForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect("dash_categories")
  
  context = {
    'form' : form
  }

  return render(request, 'dash_create_category.html', context)

def dash_create_product(request):
  form = ProductForm()
  if request.method == "POST":
    form = ProductForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect("dash_products")
  
  context = {
    'form' : form
  }

  return render(request, 'dash_create_product.html', context) 

def dash_delete_category(request, pk):
  category = Category.objects.get(pk = pk)
  category.delete()

  return redirect("dash_categories")


def dash_delete_product(request, pk):
  product = Product.objects.get(pk = pk)
  product.delete()

  return redirect("dash_products")
