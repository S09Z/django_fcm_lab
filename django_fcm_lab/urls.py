from django.contrib import admin
from django.urls import path
from messaging import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("subscribe/", views.subscribe, name="subscribe"),
    path("unsubscribe/", views.unsubscribe, name="unsubscribe"),
]
