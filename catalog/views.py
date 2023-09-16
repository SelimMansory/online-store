from catalog.forms import ProductForm, VersionForm
from catalog.models import Contact, Product, Version
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.services import get_cached_category


# Create your views here.


class ContactListView(ListView):
    """
    Контролер для вывода контактов
    """
    model = Contact
    template_name = 'catalog/contact.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
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
    template_name = 'catalog/home.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Контролер для добавления продуктов
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        if form.is_valid():
            product = form.save()
            product.owner = self.request.user
            product.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category'] = get_cached_category()
        return context_data


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context['formset'] = formset
        return context

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product')