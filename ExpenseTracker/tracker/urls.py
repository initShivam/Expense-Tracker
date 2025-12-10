from django.urls import path
from . import views
from .import models

urlpatterns = [
    path("", views.index, name='index'),
    path("delete-transaction/<int:id>/", views.delete_transaction, name='delete_transaction'),
    path("register/", views.register, name='register'),
    path("login/", views.login_view, name='login_view'),
    path("logout/", views.logout_view, name='logout_view')
]