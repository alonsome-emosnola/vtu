from django.urls import path

from . import views

urlpatterns = [
    path('accounts/', views.get_reserved_accounts, name="accounts"),
]