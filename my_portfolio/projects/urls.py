from django.urls import path
from . import views

urlpatterns = [
    path("projects_index/", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("about_index/", views.about_index, name="about_index"),
    path("", views.home, name="home"),
]