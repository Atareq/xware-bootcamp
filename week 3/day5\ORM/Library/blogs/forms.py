from django import forms

class register (forms.Form):
    username=forms.CharField(max_length=10)
    password=forms.CharField(max_length=15)
    fullname=forms.CharField(max_length=30)

class sign_in (forms.Form):
    username=forms.CharField(max_length=10)
    password=forms.CharField(max_length=15)
 
class blog (forms.Form):
    blog_title = forms.CharField(max_length=30)
    category = forms.CharField(max_length=20)
    blog = forms.Textarea()
    username = forms.CharField(max_length=15)
