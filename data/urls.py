from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="data"),
    path('data_prices/', views.data_prices, name="data_prices"),
    path('<str:serviceID>/', views.buy_data_for_self, name="buy_data"),
    path('<str:serviceID>/check_status/', views.check_status, name="check_data_status")
]