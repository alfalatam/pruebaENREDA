from django.db import models
from django.utils.timezone import now
from datetime import date
from django.conf import settings
from django.core.exceptions import ValidationError
from taggit.managers import TaggableManager


import datetime

# Create your models here.


class User(models.Model):

    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Email = models.EmailField()

    def __str__(self):
        return self.Nombre


class note(models.Model):

    class Meta:
        ordering = ['Date']

    # -----------------------ID------------------------------
    ID = models.AutoField(primary_key=True)

    # ---------------------Date-----------------------------
    Date = models.DateTimeField(default=now, editable=False)

    # -----------------------EndDate-----------------------------
    EndDate = models.DateField(
        help_text="This date must be atleast today")

    # ---------------------Note---------------------------------
    Note = models.TextField()

    # ---------------------Adjunto-----------------------------
    Adjunto = models.FileField(blank=True)

    # --------------------Relaciones--------------------------
    # user = models.ManyToManyField(User, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=False)

    # X = models.CharField(max_length=25)

    CHOICE = ((1, 'Yes'), (0, 'No'),)
#
    # ---------------------- Task----------------------------
    task = models.IntegerField(choices=CHOICE)

    # ------------------------Tags---------------------------

    tags = TaggableManager(blank=True)

    # ------------------------Type--------------------------
    Type = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return str(self.Type)
