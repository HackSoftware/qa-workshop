from django.urls import path
from . import views

urlpatterns = [
    path("nuke/", views.nuke, name="nuke"),
]
