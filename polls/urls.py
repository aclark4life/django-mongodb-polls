from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<str:pk>/", views.DetailView.as_view(), name="detail"),
    path("<str:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<str:question_id>/vote/", views.vote, name="vote"),
]
