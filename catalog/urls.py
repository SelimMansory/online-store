from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.views import ContactListView, ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from catalog.apps import CatalogConfig

# вызов функции при получении определенного запроса

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactListView.as_view(), name='contact'),
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', cache_page(180)(ProductDetailView.as_view()), name='product_details'),
    path('create_product/', never_cache(ProductCreateView.as_view()), name='create_product'),
    path('update_product/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='update_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

]