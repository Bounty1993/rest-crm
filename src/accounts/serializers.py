from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
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
            raise serializers.ValidationError(msg)
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
        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
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
            raise serializers.ValidationError(msg)

        TOKEN = 'SOME_TOKEN'
        return TOKEN


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]