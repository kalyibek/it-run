import os
from django.db import models
from django.conf import settings


IMAGES_ROOT = os.path.relpath(os.path.join(settings.MEDIA_ROOT, 'images'))


class Klass(models.Model):
    name = models.CharField(
        max_length=10
    )

    def __str__(self):
        return f'class {self.name}'


class Student(models.Model):
    first_name = models.CharField(
        max_length=50
    )
    last_name = models.CharField(
        max_length=50
    )
    photo = models.ImageField(
        upload_to=IMAGES_ROOT
    )
    klass = models.ForeignKey(
        Klass,
        on_delete=models.CASCADE
    )
    age = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

