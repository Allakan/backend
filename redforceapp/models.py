from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
import jwt


# Create your models here.

class MultipleImageField(models.ImageField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.multi_upload = True


class Advantages(models.Model):
    users = models.IntegerField()
    downloads = models.IntegerField()
    likes = models.IntegerField()
    rating = models.IntegerField()

class AdvantagesImage(models.Model):
    image1 = models.ImageField(upload_to='photos/advantages/')
    image2 = models.ImageField(upload_to='photos/advantages/')
    image3 = models.ImageField(upload_to='photos/advantages/')
    image4 = models.ImageField(upload_to='photos/advantages/')
    image5 = models.ImageField(upload_to='photos/advantages/')

class Feedback(models.Model):
    fbimage = models.ImageField(upload_to='photos/feedback/')
    name = models.CharField(max_length=80)
    STARS_CHOISES = [(i,str(i)) for i in range(1,6)]
    stars = models.IntegerField(choices=STARS_CHOISES)
    fbtext = models.TextField()

class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

class Contacts(models.Model):
    technumber = models.CharField(max_length=25)
    techmail = models.CharField(max_length=50)
    accnumber = models.CharField(max_length=25)
    accmail = models.CharField(max_length=50)

class Rating(models.Model):
    image1 = models.ImageField(upload_to='photos/rating/')
    image2 = models.ImageField(upload_to='photos/rating/')
    image3 = models.ImageField(upload_to='photos/rating/')
    image4 = models.ImageField(upload_to='photos/rating/')
    image5 = models.ImageField(upload_to='photos/rating/')
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    feedbacks = models.IntegerField()


class Subscribption(models.Model):
    quantity = models.IntegerField()
    price = models.CharField(max_length=50)
    audience = models.CharField(max_length=50)
    point1 = models.CharField(max_length=100)
    point2 = models.CharField(max_length=100)
    point3 = models.CharField(max_length=100)
    point4 = models.CharField(max_length=100)
    note = models.TextField()

class SubscribeGreen(models.Model):
    quantity = models.IntegerField()
    price = models.CharField(max_length=50)
    audience = models.CharField(max_length=50)
    point1 = models.CharField(max_length=100)
    point2 = models.CharField(max_length=100)
    point3 = models.CharField(max_length=100)
    point4 = models.CharField(max_length=100)
    note = models.TextField()


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    SUBSCRIBE_CHOICES = [
        ('not', 'not'),
        ('white', 'white'),
        ('green', 'green'),
    ]
    subscribe = models.CharField(
        max_length=10,
        choices=SUBSCRIBE_CHOICES,
        default='not',
    )