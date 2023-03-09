# -*- coding: utf-8 -*-
#class based
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy


# function based
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


from .models import Product
from .forms import ProductForm

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, "product_list.html", { "products": products,})
# #C
# def product_create(request):
#     if request.method == "POST":
#          form = ProductForm(request.POST)
#          if form.is_valid():
#             form.save()
#             return redirect(reverse("product:product_list"))
#     else:
#         form = ProductForm()
#     return render(request, "product_form.html", { "form": form, })
# #R
# def product_detail(request, pk):
#     # product = Product.objects.get(pk=pk)
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, "product_detail.html", { "product": product, })

# # PUT - several, PATCH - one
# def product_update(request, pk):
#     product_obj = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         form = ProductForm(instance=product_obj, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("product:product_detail", args=[pk,]))
#     else:
#         form = ProductForm(instance=product_obj)
#     return render(request, "product_form.html", { "form": form, "object": product_obj})


# def product_delete(request, pk):
#     product_obj = get_object_or_404(Product, pk=pk)
#     product_obj.delete()
#     return redirect(reverse("product:product_list"))




# END

class ProductList(ListView): 
    model = Product

class ProductDetail(DetailView): 
    model = Product

class ProductCreate(SuccessMessageMixin, CreateView): 
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully created!"

class ProductUpdate(SuccessMessageMixin, UpdateView): 
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully updated!"

class ProductDelete(SuccessMessageMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully deleted!"


