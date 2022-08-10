from distutils.command.upload import upload
from pydoc import describe
from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    image = models.ImageField(upload_to='media')


class Services(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    image = models.ImageField(upload_to='media')
