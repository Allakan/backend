from rest_framework import serializers
from .models import *


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