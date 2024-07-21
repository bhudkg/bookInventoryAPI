from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    OPTIONS = [
        ("s", "Science"),
        ("a", "Arts"),
        ("f", "Fiction"),
        ("d", "Drama"),
    ]


    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=10, choices=OPTIONS)

    def __str__(self):
        return self.name
