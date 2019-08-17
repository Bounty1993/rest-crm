from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer, ValidationError,
    HyperlinkedModelSerializer
)
from rest_framework.validators import UniqueValidator

from .models import Departament

User = get_user_model()


class UserRegistrationSerializer(ModelSerializer):
    password2 = serializers.CharField(label='Powtórz hasło', max_length=50)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def validate_password2(self, value):
        data = self.initial_data
        password = data.get('password')
        password2 = value
        if password != password:
            msg = 'Hasła nie różnią!'
            raise ValidationError(msg)
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=50, read_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
        ]

    def validate(self, data):
        username = data['username']
        password = data['password']
        users = User.objects.filter(username=username)
        msg = 'Użytkownik lub hasło są nieprawidłowe'
        if users.count() == 1:
            user_obj = users.first()
        else:
            raise serializers.ValidationError(msg)

        if not user_obj.check_password(password):
            raise ValidationError(msg)

        data['token'] = 'SOME_TOKEN'
        return data


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'first_name',
            'last_name', 'username',
            'email',
        ]
        extra_kwargs = {
            'username': {'read_only': True}
        }


class DepartamentSerializer(ModelSerializer):
    workers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all()
    )

    class Meta:
        model = Departament
        fields = [
            'name', 'workers'
        ]
        extra_kwargs = {
            'name': {
                'validators': [
                    UniqueValidator(queryset=Departament.objects.all())
                ]
            }
        }
