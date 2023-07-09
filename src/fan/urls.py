from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FanViewSet

router = DefaultRouter()
router.register(r'fans', FanViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
