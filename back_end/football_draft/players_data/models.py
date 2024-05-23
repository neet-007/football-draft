from django.db import models

# Create your models here.
class PositionsChoices(models.IntegerChoices):
    GK = 0, 'Goalkeeper'
    DF = 1, 'Defender'
    MF = 2, 'Midfeilder'
    FW = 3, 'Forward'

class Players(models.Model):
    first_name = models.CharField(max_length=125, db_index=True)
    middle_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125, db_index=True)
    nationality = models.CharField(max_length=125)
    age = models.IntegerField(db_index=True)
    position = models.IntegerField(choices=PositionsChoices, db_index=True)