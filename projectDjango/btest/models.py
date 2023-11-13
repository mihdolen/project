from django.db import models

class workers(models.Model):
  surname = models.CharField(max_length=30)
  name = models.CharField(max_length=30)
  otchestvo = models.CharField(max_length=30)
  pasportNumber = models.IntegerField()
  pasportSerie = models.IntegerField()
  INN = models.IntegerField()
  birth = models.DateField()
  position = models.CharField(max_length=50)








class projects(models.Model):
    title = models.CharField(max_length=50)
    satrtDate = models.DateField()
    endDate = models.DateField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

class workingOn(models.Model):
  worker = models.ForeignKey ("workers", on_delete=models.PROTECT)
  project = models.ForeignKey ("projects", on_delete=models.PROTECT)





