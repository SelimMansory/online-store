from django.urls import path
from catalog.views import ContactListView, ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from catalog.apps import CatalogConfig

# вызов функции при получении определенного запроса

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactListView.as_view(), name='contact'),
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

]