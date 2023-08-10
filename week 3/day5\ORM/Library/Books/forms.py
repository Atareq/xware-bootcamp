from django import forms

class user (forms.Form):
    username=forms.CharField(max_length=10)
    password=forms.CharField(max_length=15)
    

class blog (forms.Form):
    blog_title = forms.CharField(max_length=30)
    category = forms.CharField(max_length=20)
    blog = forms.TextField(max_length=200)
    username = forms.CharField(max_length=15)
