from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_request/", views.create_request, name="create_request"),
    path("request/<int:doc_id>/", views.view_request, name="view_request"),
]