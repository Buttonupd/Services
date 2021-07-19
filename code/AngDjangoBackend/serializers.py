from rest_framework import serializers
from .models import Tutorial
from . import models
from django.contrib.auth.hashers import make_password


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = (
            'id',
            'title',
            'description',
            'published',
        
        )
        model = models.Tutorial

def validate_password(self, value: str) -> str:
    """
    Hash value passed by user.
    :param value: password of a user
    :return: a hashed version of the password
    """
    return make_password(value)