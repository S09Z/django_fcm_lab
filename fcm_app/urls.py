# fcm_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('send_message/', views.send_message, name='send_message'),
    path('unsubscribe/<int:token_id>/', views.unsubscribe, name='unsubscribe'),
    path('signup/', views.signup, name='signup'),
]
