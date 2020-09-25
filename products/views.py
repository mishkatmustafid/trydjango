from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
# Create your views here.
from .models import Product

from .forms import ProductForm, RawProductForm


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # Now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     #print(request.GET)
#     #print(request.POST)
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # Product.objects.create(title=my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context ={
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    } # This is more efficient. Since changes in the model, doesn't require modification here.
    return render(request, "products/product_detail.html", context)

def render_initial_data(request):
    initial_data = {
        'title': "This is the awesome title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_render.html", context)

def dynamic_lookup_view(request, id):
    obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=my_id)
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context={
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    #POST request
    if request.method == 'POST':
        #Confirming delete
        obj.delete()
        return redirect('../../')
    context={
        "object": obj
    }
    return render(request, "products/product_delete.html", context)