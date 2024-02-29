from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, RegionViewSet

router = DefaultRouter()
router.register(r'agents', AgentViewSet)
router.register(r'regions', RegionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]