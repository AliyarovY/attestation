from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    number = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    birthday = serializers.DateField(required=True)


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'number',
            'birthday',
            'creation_date',
            'update_date',
        ]


    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(_('Password must be at least 8 characters long'))
        if not any(x.isdigit() for x in value):
            raise serializers.ValidationError(_('The password must include the numbers'))
        return make_password(value)

    def validate_email(self, value):
        allow_mails = ['mail.ru', 'yandex.ru']
        if all(not value.endswith('@' + x) for x in allow_mails):
            raise serializers.ValidationError(_(f'Only {allow_mails} domains are allowed for mail'))
        return value

    def validate_number(self, value):
        for i, j in enumerate(value):
            if not i and j == '+':
                continue
            if not j.isdigit():
                raise serializers.ValidationError(_('Not valid number.'))

        return value
