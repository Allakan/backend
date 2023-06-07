from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = '__all__'

class AdvantagesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvantagesImage
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class SubscribptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribption
        fields = '__all__'

class SubscribeGreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribeGreen
        fields = '__all__'


class CustomUserCreateSerializer(UserCreateSerializer):
    phone_number = serializers.CharField(required=False)
    password = serializers.CharField(write_only=False)
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)

    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('email', 'username', 'password', 'phone_number', 'subscribe')


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'
    def validate(self, attrs):
        data = super().validate(attrs)

        # Update the last_login field for the user
        user = self.user
        user.last_login = timezone.now()
        user.save()

        return data




