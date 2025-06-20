from rest_framework import serializers
from .models import Sector, WaterSystem, ElectricalSubstation, Alert

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class WaterSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterSystem
        fields = '__all__'


class ElectricalSubstationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricalSubstation
        fields = '__all__'


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'