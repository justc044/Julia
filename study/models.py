from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField('date created')
    edit_date = models.DateTimeField('date edited', blank=True, null=True)
    deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class MemberInfo(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.message