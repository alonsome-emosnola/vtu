"""
URL configuration for vtu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView, RegisterView, profile, home

from users.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('airtime/', include("airtime.urls")),
    path('data/', include("data.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("payments/", include("payments.urls")),
    path("payments/", include("referrals.urls"))
] + [

    path('user/', include('users.urls')),

    path('user/login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html', authentication_form=LoginForm), name='login'),
    
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),

    path('user/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('user/password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('user/password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('user/password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('user/password-change/', ChangePasswordView.as_view(), name='password_change'),

    re_path(r'^oauth/', include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

