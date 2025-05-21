from django.urls import path

from restaurant.apps import RestaurantConfig
from restaurant.views import (
    HomeListView,
    HomeView,
    OrderCreateView,
    OrderDeleteView,
    OrderDetailView,
    OrderListAdminView,
    OrderListView,
    OrderUpdateView,
    TableCreateView,
    TableDeleteView,
    TableDetailView,
    TableUpdateView,
)

app_name = RestaurantConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("table/table_list/", HomeListView.as_view(), name="table_list"),
    path("table/table_create/", TableCreateView.as_view(), name="table_create"),
    path("table/table_update/<int:pk>/", TableUpdateView.as_view(), name="table_update"),
    path("table/table_detail/<int:pk>/", TableDetailView.as_view(), name="table_detail"),
    path("table/table_order_detail/<int:pk>/", TableDetailView.as_view(), name="table_order_detail"),
    path("table/table_delete/<int:pk>/", TableDeleteView.as_view(), name="table_delete"),
    path("table/order_list/", OrderListView.as_view(), name="order_list"),
    path("table/order_list_admin/", OrderListAdminView.as_view(), name="order_list_admin"),
    path("table/order_create/", OrderCreateView.as_view(), name="order_create"),
    path("table/order_update/<int:pk>/", OrderUpdateView.as_view(), name="order_update"),
    path("table/order_delete/<int:pk>/", OrderDeleteView.as_view(), name="order_delete"),
    path("table/order_detail/<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
]
