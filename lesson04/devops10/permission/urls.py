from django.urls import path, re_path

from . import views

urlpatterns = [
    # FBV django
    path('v1/casbin/auth', views.CheckRestApiPermission.as_view()),
]