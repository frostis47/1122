from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from users.forms import UserRegistrationForm
from users.models import User

from .forms import UserForm

# Payment


class RegisterView(CreateView):
    """Метод для регистраций user"""

    model = User
    template_name = "register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        response = super().form_valid(form)

        send_mail(
            subject="Добро пожаловать!",
            message='Спасибо за регистрацию на нашем сайте "__"',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[form.cleaned_data.get("email")],
            fail_silently=False,
        )

        return response


class UserListView(ListView):
    """Метод просмотров всех user"""

    model = User
    template_name = "user_list.html"
    context_object_name = "users"

    # def get_queryset(self):
    #     queryset = cache.get('user_queryset')
    #     if not queryset:
    #         queryset = super().get_queryset()
    #         cache.set('user_queryset', queryset, 60 * 2)
    #     return queryset


class UserCreateView(LoginRequiredMixin, CreateView):
    """Метод для создания user"""

    model = User
    form_class = UserForm
    success_url = reverse_lazy("user_list")


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """Метод для изменения user"""

    model = User
    form_class = UserForm
    template_name = "user_form.html"
    success_url = reverse_lazy("users:user_list")


class UserDeleteView(DeleteView):
    """Метод для удаления user"""

    model = User
    template_name = "user_delete.html"
    success_url = reverse_lazy("user_list")