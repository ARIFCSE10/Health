from django.db import models

# Create your models here.
class blog(models.Model):

    title = models.CharField(max_length=255)
    body = models.CharField(max_length=1000)

    class Meta:
        db_table = 'blog'
        verbose_name = ("blog")
        verbose_name_plural = ("blogs")
