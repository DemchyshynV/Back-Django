from rest_framework import serializers, status
from rest_framework.generics import get_object_or_404

from .models import UserModel, ProfileModel


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ['phone']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = ['username', 'password', 'email', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()
        ProfileModel.objects.create(user=user, **profile)
        return user


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('is_superuser',)


class GetUserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id']
