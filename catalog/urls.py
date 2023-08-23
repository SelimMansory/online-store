from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact, StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, \
    StudentDeleteView, toggle_activity

app_name = CatalogConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('view/<int:pk>/', StudentDetailView.as_view(), name='view_student'),
    path('create/', StudentCreateView.as_view(), name='create_student'),
    path('edit/<int:pk>', StudentUpdateView.as_view(), name='update_student'),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name='delete_student'),
    path('activity/<int:pk>', toggle_activity, name='toggle_activity'),
]
