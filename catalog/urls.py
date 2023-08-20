from django.urls import path
from catalog.views import HomeListView, ContactListView, ProductDetailView, ProductListView, ProductCreateView
from catalog.apps import CatalogConfig
# вызов функции при получении определенного запроса

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactListView.as_view(), name='contact'),
    path('product/', ProductListView.as_view(), name='product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('create_product/', ProductCreateView.as_view(), name='create_product')
]