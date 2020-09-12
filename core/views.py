from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from core.models import Product
from django.urls import reverse_lazy

class IndexView(ListView):
    models = Product
    template_name = 'index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

class CreateProduct(CreateView):
    model = Product
    template_name = 'product_form.html'
    queryset = Product.objects.all()
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('index')

class UpdateProduct(UpdateView):
    model = Product
    template_name = 'product_form.html'
    queryset = Product.objects.all()
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('index')

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'product_del.html'
    queryset = Product.objects.all()
    success_url = reverse_lazy('index')
