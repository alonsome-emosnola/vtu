from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="airtime"),
    path('<str:serviceID>/', views.buy_airtime_for_self, name="airtime"),
    path('<str:serviceID>/check_status/', views.check_airtime_status, name="check_airtime_status")
]