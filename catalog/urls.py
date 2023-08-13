from django.urls import path
from catalog.views import home, contact, ProductDetailView, product
from catalog.apps import CatalogConfig
# вызов функции при получении определенного запроса

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contact, name='contact'),
    path('product/', product, name='product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_details')
]