from django.shortcuts import render
from django.core import management
from catalog.models import Contact, Product
from datetime import datetime
from django.views.generic import DetailView


# Create your views here.


def home(request):
    product_list = Product.objects.all()
    contex = {'object_list': product_list,
              'object_img': '23052.jpg'}
    management.call_command('last_five')
    return render(request, 'main/home.html', context=contex)


def contact(request):
    contact_list = Contact.objects.all()
    context = {'object_list': contact_list}
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)

    return render(request, 'main/contact.html', context=context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_details.html'
    context_object_name = 'article'


def product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        price = request.POST.get('price')
        Product.objects.create(name=name, description=description, category=category, price=price,
                               create_date=datetime.now(), date_of_change=datetime.now())

    product_list = Product.objects.all()
    contex = {'object_list': product_list,
              'object_img': '23052.jpg'}
    return render(request, 'main/product.html', context=contex)