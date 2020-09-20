from rest_framework import routers

from . import views


ticket_router = routers.DefaultRouter()
ticket_router.register(r'classify', views.ClassifyModelViewSet, basename="classify")
ticket_router.register(r'tpl', views.TplInfoModelViewSet, basename="tpl")