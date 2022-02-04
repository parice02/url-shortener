from django.db import models

# Create your models here.


class Url(models.Model):
    long_form = models.URLField(unique=True, max_length=300)
    added_at = models.DateTimeField(auto_now_add=True)


class Shortener(models.Model):
    url = models.OneToOneField(Url, on_delete=models.PROTECT)
    short_form = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField()
