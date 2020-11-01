from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.TaskListView.as_view(), name="list"),
    path("catlist/", views.CatListView.as_view(), name="catlist"),
    path("priolist/", views.PrioListView.as_view(), name="priolist"),
    path("list/c/<slug:cat_slug>", views.tasks_by_cat, name="list_by_cat"),
    path("list/p/<int:prio_pk>", views.tasks_by_prio, name="list_by_prio"),
    path("details/<int:pk>", views.TaskDetailsView.as_view(), name="details"),
    path("datetime", views.just_datetime, name="datetime"),
]
