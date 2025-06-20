from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SectorViewSet, WaterSystemViewSet, ElectricalSubstationViewSet, AlertViewSet, main_panel, sectors_view, water_system_view, substation_view

router = DefaultRouter()
router.register(r'sector', SectorViewSet)
router.register(r'water-system', WaterSystemViewSet)
router.register(r'substation', ElectricalSubstationViewSet)
router.register(r'alert', AlertViewSet)

urlpatterns = [
    path('', main_panel, name='panel'),
    path('sectors/', sectors_view, name="sectors"),
    path('waters-systems/', water_system_view, name="water"),
    path('substations/', substation_view, name="substation"),
    path('api/', include(router.urls)),
]