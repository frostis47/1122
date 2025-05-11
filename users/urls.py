from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserCreateView, UserDeleteView, UserListView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("user/", UserListView.as_view(), name="user_list"),
    path("user/create/", UserCreateView.as_view(), name="user_create"),
    path("user/update/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
    path("user/delete/<int:pk>/", UserDeleteView.as_view(), name="user_delete"),
]
