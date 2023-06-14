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
from django.contrib.auth.password_validation import validate_password
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q

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

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        if email is None:
            return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Проверка наличия пользователя с заданным email
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User with the provided email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        # Возвращаем только id пользователя
        return Response({'id': user.id}, status=status.HTTP_200_OK)

class CustomUserUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer
    def partial_update(self, request, *args, **kwargs):
        if 'password' in request.data:
            request.data['password'] = make_password(request.data['password'])
            
        return super().partial_update(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        if 'password' in request.data:
            request.data['password'] = make_password(request.data['password'])

        return super().update(request, *args, **kwargs)
 
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        email = request.data.get('email')
        username = request.data.get('username')
        new_password = request.data.get('password')
        
        if CustomUser.objects.filter(phone_number=phone_number).exists() or \
                CustomUser.objects.filter(email=email).exists() or \
                CustomUser.objects.filter(username=username).exists():
            user = CustomUser.objects.get(Q(phone_number=phone_number) & Q(email=email) & Q(username=username))
            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Password updated successfully.'}, status=status.HTTP_200_OK)
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
    

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
