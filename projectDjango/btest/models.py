from django.db import models

class workers(models.Model):
  surname = models.CharField(max_length=30,verbose_name="Фамилия")
  name = models.CharField(max_length=30, verbose_name="Имя")
  otchestvo = models.CharField(max_length=30,verbose_name="Отчество")
  pasportNumber = models.IntegerField(verbose_name="Номер паспорта")
  pasportSerie = models.IntegerField(verbose_name="Серия паспорта")
  INN = models.IntegerField(verbose_name="ИНН")
  birth = models.DateField(verbose_name="Дата рождения")
  position = models.CharField(max_length=50,verbose_name="Должность")
  def __str__(self):
    return self.surname
  class Meta:
    verbose_name_plural = 'Сотрудник'
    verbose_name = 'Сотрудники'
    ordering = ['surname']





class projects(models.Model):
    title = models.CharField(max_length=50,verbose_name="Название")
    satrtDate = models.DateField(verbose_name="Дата начала")
    endDate = models.DateField(null=True, blank=True,verbose_name="Дата окончания")
    price = models.FloatField(null=True, blank=True,verbose_name="Объём финансирования")
    def __str__(self):
      return self.title
    
    class Meta:
      verbose_name_plural = 'Проект'
      verbose_name = 'Проекты'
      ordering = ['satrtDate']
    

class workingOn(models.Model):
  worker = models.ForeignKey ("workers", on_delete=models.PROTECT,verbose_name="Сотрудник")
  project = models.ForeignKey ("projects", on_delete=models.PROTECT,verbose_name="Проект")
  def __str__(self):
      return self.project.title  +"  " + self.worker.surname


  class Meta:
      verbose_name_plural = 'Участие в проектах'
      verbose_name = 'Участия в проектах'




