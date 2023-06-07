from django.shortcuts import render
from rest_framework import generics, permissions
from .models import *
from .serializers import *
from .permissions import *
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from datetime import timedelta, datetime
from django.utils import timezone

# Create your views here.

class AdvantagesList(generics.ListCreateAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer
    permission_classes = (IsAdminOrReadOnly, )

class AdvantagesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer
    permission_classes = (IsAdminOrReadOnly, )

class AdvantagesImageList(generics.ListCreateAPIView):
    queryset = AdvantagesImage.objects.all()
    serializer_class = AdvantagesImageSerializer
    permission_classes = (IsAdminOrReadOnly, )

class AdvantagesImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdvantagesImage.objects.all()
    serializer_class = AdvantagesImageSerializer
    permission_classes = (IsAdminOrReadOnly, )

class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAdminOrReadOnly, )

class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAdminOrReadOnly, )

class FaqList(generics.ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    permission_classes = (IsAdminOrReadOnly, )

class FaqDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    permission_classes = (IsAdminOrReadOnly, )

class ContactsList(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = (IsAdminOrReadOnly, )

class ContactsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = (IsAdminOrReadOnly, )

class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAdminOrReadOnly, )

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAdminOrReadOnly, )

class SubscribptionList(generics.ListCreateAPIView):
    queryset = Subscribption.objects.all()
    serializer_class = SubscribptionSerializer
    permission_classes = (IsAdminOrReadOnly, )

class SubscribptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscribption.objects.all()
    serializer_class = SubscribptionSerializer
    permission_classes = (IsAdminOrReadOnly, )

class SubscribeGreenList(generics.ListCreateAPIView):
    queryset = SubscribeGreen.objects.all()
    serializer_class = SubscribeGreenSerializer
    permission_classes = (IsAdminOrReadOnly, )

class SubscribeGreenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscribeGreen.objects.all()
    serializer_class = SubscribeGreenSerializer
    permission_classes = (IsAdminOrReadOnly, )


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
class CustomUserUpdateList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer


class CustomUserUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer
    def partial_update(self, request, *args, **kwargs):
        # Hash the password if present in the request data
        if 'password' in request.data:
            request.data['password'] = make_password(request.data['password'])

        return super().partial_update(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        # Hash the password if present in the request data
        if 'password' in request.data:
            request.data['password'] = make_password(request.data['password'])

        return super().update(request, *args, **kwargs)
    

from rest_framework.views import APIView
from rest_framework.response import Response

class CustomUserStats(APIView):
    def get(self, request, format=None):
        total_users = CustomUser.objects.count()
        white_subscribers = CustomUser.objects.filter(subscribe='white').count()
        green_subscribers = CustomUser.objects.filter(subscribe='green').count()

        five_minutes_ago = timezone.now() - timezone.timedelta(minutes=5)
        online_users = CustomUser.objects.filter(last_login__gte=five_minutes_ago).count()

        
        data = {
            'total_users': total_users,
            'white_subscribers': white_subscribers,
            'green_subscribers': green_subscribers,
            'online_users': online_users,
        }
        
        return Response(data)
