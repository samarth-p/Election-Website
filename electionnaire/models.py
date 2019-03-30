from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class User(AbstractUser):
    @property
    def is_voter(self):
        if hasattr(self, 'voter'):
            return True
        return False

    @property
    def is_eci(self):
        if hasattr(self, 'eci'):
            return True
        return False


class Party(models.Model):
    name = models.CharField(max_length=50)
    symbols = models.ImageField(upload_to='symbols/')

    def __str__(self):
        return self.name


class Constituency(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    id = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='candidates/')
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Eci(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    voter_id = models.CharField(primary_key='True', max_length=100)
    aadhar_no = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, unique=True)
    voted = models.BooleanField(default=False)
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    post_time = models.DateTimeField(default=timezone.now, blank=False)
    caption = models.CharField(max_length=200)
    severity = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
     )
    severity_eci = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
     )
