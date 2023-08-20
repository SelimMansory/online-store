from django.shortcuts import render
from django.core import management
from catalog.models import Contact, Product
from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy


# Create your views here.


class HomeListView(ListView):
    """
    Контролер для вывода домашней страницы
    """
    model = Product
    template_name = 'catalog/home.html'


class ContactListView(ListView):
    """
    Контролер для вывода контактов
    """
    model = Contact
    template_name = 'catalog/contact.html'


class ProductDetailView(DetailView):
    """
    Контролер для детальной информации продуктов
    """
    model = Product
    context_object_name = 'article'


class ProductListView(ListView):
    """
    Контролер для показа продуктов
    """
    model = Product


class ProductCreateView(CreateView):
    """
    Контролер для добавления продуктов
    """
    model = Product
    fields = ('name', 'description', 'category', 'price')
    success_url = reverse_lazy('catalog:product')