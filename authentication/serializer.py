from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=30)

# class UserRegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }
#
#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         user = User.objects.create(**validated_data)
#         return user
#
#
# class UserLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']
