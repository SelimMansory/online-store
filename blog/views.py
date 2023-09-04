from django.shortcuts import render
from blog.models import Blog
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from pytils.translit import slugify


# Create your views here.


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'context', 'preview')
    success_url = reverse_lazy('blog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        if self.object.count_views == 100:
            subject = 'Условие выполнено'
            message = 'Условие было выполнено.'
            from_email = 'EMAIL'
            recipient_list = ['EMAIL']  # Укажите адрес получателя
            send_mail(subject, message, from_email, recipient_list)
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'context', 'preview')

    def get_success_url(self):
        return reverse_lazy('blog:view', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog')