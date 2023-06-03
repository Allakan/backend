from django.shortcuts import render
from rest_framework import generics, permissions
from .models import *
from .serializers import *
from .permissions import *
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
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
