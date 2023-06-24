from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from storages.backends.gcloud import GoogleCloudStorage

# Create your models here.


class Advantages(models.Model):
    users = models.IntegerField()
    downloads = models.IntegerField()
    likes = models.IntegerField()
    rating = models.IntegerField()

class AdvantagesImage(models.Model):
    image1 = models.ImageField(upload_to='advantages/', storage=GoogleCloudStorage())
    image1_name = models.CharField(max_length=255, blank=True)
    
    image2 = models.ImageField(upload_to='advantages/', storage=GoogleCloudStorage())
    image2_name = models.CharField(max_length=255, blank=True)
    
    image3 = models.ImageField(upload_to='advantages/', storage=GoogleCloudStorage())
    image3_name = models.CharField(max_length=255, blank=True)
    
    image4 = models.ImageField(upload_to='advantages/', storage=GoogleCloudStorage())
    image4_name = models.CharField(max_length=255, blank=True)
    
    image5 = models.ImageField(upload_to='advantages/', storage=GoogleCloudStorage())
    image5_name = models.CharField(max_length=255, blank=True)
    

class Feedback(models.Model):
    fbimage = models.ImageField(upload_to='feedback/', storage=GoogleCloudStorage())
    image1_name = models.CharField(max_length=255, blank=True)
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
    image1 = models.ImageField(upload_to='raiting/', storage=GoogleCloudStorage())
    image1_name = models.CharField(max_length=255, blank=True)
    
    image2 = models.ImageField(upload_to='raiting/', storage=GoogleCloudStorage())
    image2_name = models.CharField(max_length=255, blank=True)
    
    image3 = models.ImageField(upload_to='raiting/', storage=GoogleCloudStorage())
    image3_name = models.CharField(max_length=255, blank=True)
    
    image4 = models.ImageField(upload_to='raiting/', storage=GoogleCloudStorage())
    image4_name = models.CharField(max_length=255, blank=True)
    
    image5 = models.ImageField(upload_to='raiting/', storage=GoogleCloudStorage())
    image5_name = models.CharField(max_length=255, blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    feedbacks = models.IntegerField()


class Subscribption(models.Model):
    quantity = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    audience = models.CharField(max_length=50)
    point1 = models.CharField(max_length=100)
    point2 = models.CharField(max_length=100)
    point3 = models.CharField(max_length=100)
    point4 = models.CharField(max_length=100)
    note = models.TextField()

class SubscribeGreen(models.Model):
    quantity = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    audience = models.CharField(max_length=50)
    point1 = models.CharField(max_length=100)
    point2 = models.CharField(max_length=100)
    point3 = models.CharField(max_length=100)
    point4 = models.CharField(max_length=100)
    note = models.TextField()
@receiver(pre_save, sender=SubscribeGreen)
def add_currency_symbol(sender, instance, **kwargs):
    instance.price = f'{instance.price} ₽' 


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