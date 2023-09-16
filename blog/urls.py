from django.urls import path
from django.views.decorators.cache import never_cache

from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogDeleteView, BlogUpdateView
from blog.apps import BlogConfig
# вызов функции при получении определенного запроса

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('create/', never_cache(BlogCreateView.as_view()), name='create'),
    path('update/<int:pk>/', never_cache(BlogUpdateView.as_view()), name='update'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),

]