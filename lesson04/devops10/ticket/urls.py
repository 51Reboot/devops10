from django.urls import path, re_path

from . import views

urlpatterns = [
    path('task', views.TaskAPIView.as_view()),
]