from django.db import models

class Sector(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.code})"


class WaterSystem(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    flow_liters_per_min = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class ElectricalSubstation(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    kv_voltage = models.FloatField()
    kw_consupmtion = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Alert(models.Model):
    alert_type = models.CharField(max_length=100)
    description = models.TextField()
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    timestamp =  models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=[("HIGH", "High"), ("MEDIUM", "Medium"), ("LOW", "Low")])