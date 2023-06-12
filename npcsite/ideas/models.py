from django.db import models
from django.db import models
from django.contrib.auth.models import User
import random
import string

def generate_unique_code():
    length = 9  # set code length to 9

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Topic.objects.filter(code=code).count() == 0:
            break
    
    return code

class Topic(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=9, default=generate_unique_code, unique=True)
    creator = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
