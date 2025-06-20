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


class ElectricalSubstationViewSet(viewsets.ModelViewSet):
    queryset = ElectricalSubstation.objects.all()
    serializer_class = ElectricalSubstationSerializer


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


def main_panel(request):
    return render(request, 'main_panel.html')

def sectors_view(request):
    sectors = Sector.objects.all()
    return render(request, 'sectors.html', {'sectors': sectors})

def water_system_view(request):
    data = WaterSystem.objects.all().order_by('-timestamp')[:10]
    return render(request, 'water_systems.html', {'data': data})

def substation_view(request):
    substations = ElectricalSubstation.objects.all().order_by('-timestamp')[:10]
    return render(request, 'substations.html', {'substations': substations })