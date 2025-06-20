from django.shortcuts import render
from rest_framework import viewsets
from .models import Sector, WaterSystem, ElectricalSubstation, Alert
from .serializers import SectorSerializer, WaterSystemSerializer, ElectricalSubstationSerializer, AlertSerializer

class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


class WaterSystemViewSet(viewsets.ModelViewSet):
    queryset = WaterSystem.objects.all()
    serializer_class = WaterSystemSerializer


class ElectrocalSubstationViewSet(viewsets.ModelViewSet):
    queryset = ElectricalSubstation.objects.all()
    serializer_class = ElectricalSubstationSerializer


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer