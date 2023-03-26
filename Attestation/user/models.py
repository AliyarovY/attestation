from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import DateAbstractModel, NULLABLE


class User(AbstractUser, DateAbstractModel):
    number = models.CharField(max_length=100)
    birthday = models.DateField(**NULLABLE)


    class Meta:
        db_table = 'user'
