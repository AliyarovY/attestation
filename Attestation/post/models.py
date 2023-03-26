from django.db import models

from base.models import DateAbstractModel, UserFKeyAbstractModel, NULLABLE


class Post(
    UserFKeyAbstractModel,
    DateAbstractModel,
):
    headline = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/post/', **NULLABLE)


    class Meta:
        db_table = 'post'
