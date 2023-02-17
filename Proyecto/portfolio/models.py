from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='imgs/')
    url = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Projects'

    def __str__(self):
       return self.title

class Certificaciones(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='imgs/')
    url = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Certificaciones'

    def __str__(self):
       return self.title