from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.forms import UserRegisterForm, UserProfiledForm
from users.models import User
from users.services import _send_mail, random_key, create_password


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save()
            key = random_key()
            new_user.mail_key = key
            new_user.is_active = False
            new_user.save()
            _send_mail('Верификация', f'http://127.0.0.1:8000/users/verification/?key={key}', new_user.email)

        return super().form_valid(form)


def verification(request):
    key = request.GET.get('key')
    users = User.objects.all()
    for user in users:
        if key == user.mail_key:
            user.is_active = True
            user.save()
            break
    return redirect('catalog:home')


def forgotten_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email)[0]
        if user:
            password = create_password()
            user.set_password(password)
            user.save()
            _send_mail('Новый пароль', f'Новый пароль: {password}', email)
            return redirect('catalog:home')

    return render(request, 'users/forgotten_password.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfiledForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user