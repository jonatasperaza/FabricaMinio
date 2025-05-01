from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.uploader.views import ArchiveViewSet

router = DefaultRouter()
router.register(r"archives", ArchiveViewSet, basename="arquivos")

urlpatterns = [
    path("api/", include(router.urls)),
]
