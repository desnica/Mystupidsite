from django.urls import path

from . import viewsblog

urlpatterns = [
        path("", viewsblog.blog1, name="blog1"),
    ]