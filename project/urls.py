from django.urls import path
from app import views
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
]
