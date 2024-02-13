from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("category/<int:catalog_id>/", views.category),
]
