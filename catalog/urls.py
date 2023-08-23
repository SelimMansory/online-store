from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact, StudentListView, StudentDetailView
app_name = CatalogConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('view/<int:pk>/', StudentDetailView.as_view(), name='view_student'),
]
