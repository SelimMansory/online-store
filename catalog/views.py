from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'catalog/index.html'


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contact.html', context)


class StudentDetailView(DetailView):
    model = Student
    template_name = 'catalog/student_detail.html'
