from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkerViewSet

router = DefaultRouter()
router.register(r'workers', WorkerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]