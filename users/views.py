from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from users.forms import UserRegistrationForm
from users.models import User
from .forms import UserForm

class RegisterView(CreateView):
    """Метод для регистрации пользователя"""

    model = User
    template_name = "register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        try:
            send_mail(
                subject="Добро пожаловать!",
                message='Спасибо за регистрацию на нашем сайте "__"',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[form.cleaned_data.get("email")],
                fail_silently=False,
            )
        except Exception as e:
            form.add_error(None, "Ошибка при отправке письма: {}".format(e))
            return self.form_invalid(form)
        return super().form_valid(form)


class UserListView(ListView):
    """Метод просмотра всех пользователей"""

    model = User
    template_name = "user_list.html"
    context_object_name = "users"

class UserCreateView(LoginRequiredMixin, CreateView):
    """Метод для создания пользователя"""

    model = User
    form_class = UserForm
    success_url = reverse_lazy("user_list")

class UserUpdateView(LoginRequiredMixin, UpdateView):
    """Метод для изменения пользователя"""

    model = User
    form_class = UserForm
    template_name = "user_form.html"
    success_url = reverse_lazy("users:user_list")

class UserDeleteView(DeleteView):
    """Метод для удаления пользователя"""

    model = User
    template_name = "user_delete.html"
    success_url = reverse_lazy("user_list")
