from rest_framework import serializers
from django.contrib.auth.models import User
from .core import models


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.username = validate_data.get('username')
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if len(users) != 0:
            raise serializers.ValidationError(
                "Este usuario ya existe, por favor ingresa uno nuevo.")
        else:
            return data

    def validate_email(self, data):
        emails = User.objects.filter(email=data)
        if len(emails) != 0:
            raise serializers.ValidationError(
                "Este email ya existe, por favor ingresa uno nuevo.")
        else:
            return data


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CrearEvento
        fields = ['id', 'event_name', 'event_category', 'event_place', 'event_address',
                  'event_initial_date', 'event_final_date', 'event_type', 'thumbnail']
