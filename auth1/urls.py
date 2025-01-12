from django.urls import path

from . import views

urlpatterns = [
        path("", views.authing, name="authing"),
    ]