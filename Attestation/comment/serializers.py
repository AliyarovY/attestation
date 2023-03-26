from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    text = serializers.CharField(max_length=1_000, required=True)


    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
            'creation_date',
            'update_date',
            'post',
        ]
        write_only_fields = ['post']
