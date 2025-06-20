from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SectorViewSet, WaterSystemViewSet, ElectrocalSubstationViewSet, AlertViewSet

router = DefaultRouter()
router.register(r'sector', SectorViewSet)
router.register(r'water-system', WaterSystemViewSet)
router.register(r'substation', ElectrocalSubstationViewSet)
router.register(r'alert', AlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
]