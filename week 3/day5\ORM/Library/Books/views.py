from django.shortcuts import render, redirect
from django import forms 
from django.http import HttpResponse 

from .models import *

def base(request):
    
    return render(request, 'base.html')

def signup(request):
    # if form(request.post):
    #     re

    return render(request, 'sign_up.html', {'form': 'form'})

def signin(request):
    return render(request, 'sign_in.html')


# # def create_book(request):
#     # Create a new Book object using the create() method
#     Book.objects.create(title='Sample Book', author='John Doe', publication_date='2023-08-07')


 

# def save(request):
#     if request.method == 'POST':  # Correct the method to uppercase 'POST'
#         form= request.form()
#         if form.isvalid():
       
def signin(request):
   return render(request,'sign_in.html')
