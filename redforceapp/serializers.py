from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import timezone

class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = '__all__'

class AdvantagesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvantagesImage
        fields = '__all__'

    def get_image1_name(self, obj):
        return f'https://storage.cloud.google.com/testrfbucket/{obj.image1.name}'

    def get_image2_name(self, obj):
        return f'https://storage.cloud.google.com/testrfbucket/{obj.image2.name}'

    def get_image3_name(self, obj):
        return f'https://storage.cloud.google.com/testrfbucket/{obj.image3.name}'

    def get_image4_name(self, obj):
        return f'https://storage.cloud.google.com/testrfbucket/{obj.image4.name}'

    def get_image5_name(self, obj):
        return f'https://storage.cloud.google.com/testrfbucket/{obj.image5.name}'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
    def fbimage_name(self, obj):
        return f'https://storage.cloud.google.com/testrfbucket/{obj.fbimage.name}'

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
    def get_image1_name(self, obj):
        return f'https://storage.cloud.google.com/testrfbucket/{obj.image1.name}'

    def get_image2_name(self, obj):
        return f'https://storage.cloud.google.com/testrfbucket/{obj.image2.name}'

    def get_image3_name(self, obj):
        return f'https://storage.cloud.google.com/testrfbucket/{obj.image3.name}'

    def get_image4_name(self, obj):
        return f'https://storage.cloud.google.com/testrfbucket/{obj.image4.name}'

    def get_image5_name(self, obj):
        return f'https://storage.cloud.google.com/testrfbucket/{obj.image5.name}'

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

        user = self.user
        user.last_login = timezone.now()
        user.save()

        return data




