# django_fcm_lab/urls.py
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from fcm_app import views as fcm_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fcm_views.home, name='home'),
    path('fcm/', include('fcm_app.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
