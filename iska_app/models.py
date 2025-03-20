from django.db import models
from cloudinary.models import CloudinaryField


class Carousel (models.Model):
    title = models.CharField(max_length=100)
    text_button = models.CharField(max_length=50)
    image = CloudinaryField('image', resource_type='image')

    def __str__(self):
        return self.title
    

class Service(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=200)
    description = models.TextField(max_length=500)
    text_button = models.CharField(max_length=50)
    image = CloudinaryField('image', resource_type='image')
    key_words = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField(max_length=500)

    def __str__(self):
        return self.question
    

class Team(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = CloudinaryField('image', resource_type='image')

    def __str__(self):
        return self.full_name
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=4000)
    image = CloudinaryField('image', resource_type='image')

    def __str__(self):
        return self.title
    