from django.urls import path, include
from rest_framework import routers

from app import views

router = routers.DefaultRouter()
router.register(r"cats", views.CatVewSet)

urlpatterns = [
    path("cats/", include(router.urls)),
]
