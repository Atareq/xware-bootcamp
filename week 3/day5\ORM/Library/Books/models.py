from typing import Any, Mapping, Optional, Type, Union
from django.db import models
from django import forms
from django.db.models import OneToOneField, CASCADE  # Import OneToOneField and CASCADE

class user (models.Model):
    fullname=models.CharField()
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=15)

class blog (models.Model):
    blog_title = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    blog = models.TextField(max_length=200)
    username = models.CharField(max_length=15)

 
# class Book(forms.Form):
#     name = forms.CharField(max_length=50)
#     price = forms.IntegerField()
#     published_year = forms.IntegerField()
#     published = forms.DateField(required=False)  # Use 'required=False' instead of 'null=True'
#     available = forms.BooleanField(initial=True)
#     author = forms.IntegerField()

# class BookDetail(forms.Form):
#     language = forms.CharField(max_length=100)
#     page_count = forms.IntegerField()
#     book = OneToOneField(Book, on_delete=forms.CASCADE)  # Use OneToOneField from django.db.models
