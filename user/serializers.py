from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import Profile, ProfileRole

class ProfileSerializer(serializers.ModelSerializer):
    profile_role_id = serializers.IntegerField(write_only=True,required=True)
    class Meta:
        model = Profile
        exclude = ('user',)

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email','password','profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        profile_role_id = profile_data.pop('profile_role_id')
        user = User(**validated_data)
        user.save()
        profile_role = ProfileRole.objects.get(id=profile_role_id)
        Profile.objects.create(user=user, profile_role=profile_role)
        print("===>>>>", profile_role)
        return user

class UserSerializerSimple(UserSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
