from django.contrib.auth import get_user
from django.utils.timezone import datetime
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from comment.serializers import CommentSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


    class Meta:
        model = Post
        fields = [
            'headline',
            'text',
            'image',
            'author',
            'comments',
            'creation_date',
            'update_date',
        ]


    def validate_headline(self, value):
        bad_words = 'ерунда, глупость, чепуха'.split(', ')
        if any(x in value for x in bad_words):
            raise serializers.ValidationError(_('Bad words in headline'))
        return value

    def validate(self, data):
        '''
        Validation of age
        '''
        current_year = datetime.now().year
        bithday_year = data['author'].birthday.year
        age = current_year - bithday_year
        if age < 18:
            raise serializers.ValidationError(_('The author\'s age must be over 18'))

        return data
