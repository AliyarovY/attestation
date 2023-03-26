from django.db import models

from base.models import DateAbstractModel, UserFKeyAbstractModel, NULLABLE


class Comment(
    UserFKeyAbstractModel,
    DateAbstractModel,
):
    post = models.ForeignKey(
        'post.Post',
        related_name='comments',
        on_delete=models.CASCADE
    )


    class Meta:
        db_table = 'comment'
