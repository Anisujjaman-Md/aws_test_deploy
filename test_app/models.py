from django.db import models
from django.db.models import F

class Square(models.Model):
    side = models.IntegerField()
    area = models.GeneratedField(
        expression=F("side") * F("side"),
        output_field=models.BigIntegerField(),
        db_persist=True,
    )