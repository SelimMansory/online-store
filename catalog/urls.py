from django.urls import path
from catalog.views import home, contact

# вызов функции при получении определенного запроса
urlpatterns = [
    path('', home),
    path('contacts/', contact)
]