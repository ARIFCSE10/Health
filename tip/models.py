from django.db import models

# Create your models here.
class tip(models.Model):

    title = models.CharField(max_length=255)
    body = models.CharField(max_length=1000)

    class Meta:
        db_table = 'tip'
        verbose_name = ("tip")
        verbose_name_plural = ("tips")
