from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("list/", views.UsersListView.as_view(), name="user_list"),
    path("create/", views.UserCreateView.as_view(), name="users_create"),
    path("update/<int:pk>/", views.UserUpdateView.as_view(), name="users_update"),
    path("delete/<int:pk>/", views.UserDeleteView.as_view(), name="users_delete"),
]
