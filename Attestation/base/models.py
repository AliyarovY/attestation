from django.db import models


NULLABLE = dict(null=True, blank=True)


class DateAbstractModel(models.Model):
    """Abstract class with date"""

    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)


    class Meta:
        abstract = True


class UserFKeyAbstractModel(models.Model):
    """
    Abstract class for models related by
    the ForeignKey type to the User
    """

    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    text = models.TextField(**NULLABLE)


    class Meta:
        abstract = True
