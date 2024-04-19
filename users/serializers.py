from rest_framework import serializers
from .models import User
from .models import User, Payment
from django.contrib.auth.hashers import make_password


def create(validated_data):
    """Хэширование пароля перед сохранением пользователя"""
    validated_data['password'] = make_password(validated_data['password'])
    user = User.objects.create(**validated_data)
    return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'email', 'phone', 'city', 'avatar']


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'payment_date', 'course', 'lesson', 'amount', 'payment_method']
