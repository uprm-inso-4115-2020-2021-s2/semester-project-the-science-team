from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Booth(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    cover_image = models.ImageField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booth')


class Artwork(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    image = models.ImageField()
    price = models.FloatField()
    interested = models.BooleanField(default=False)
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE, related_name='artworks')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    is_artisan = models.BooleanField(default=False)
    has_booth = models.BooleanField(default=False)


