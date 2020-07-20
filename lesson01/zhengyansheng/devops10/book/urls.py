from django.urls import path, re_path

from book.views.v1 import views as v1_view

urlpatterns = [
    path('v1/publish', v1_view.PublishView),
    path('v1/publish_v1', v1_view.PublishViewV2.as_view()),
]