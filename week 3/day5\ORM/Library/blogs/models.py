from django.db import models
from django.db import models
from django.shortcuts import render
from django.contrib.auth import logout ,login
from django.contrib.auth import authenticate

class User(models.Model):
    fullname=models.CharField(max_length=30)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=15)

class blog(models.Model):
    blog_title = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    blog = models.TextField(max_length=200)
    username = models.CharField(max_length=15)