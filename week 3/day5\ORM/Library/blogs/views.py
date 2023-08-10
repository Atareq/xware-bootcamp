from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .forms import register , sign_in
from .urls import *

def authenticate(request):
    if request.user.is_authenticated:
        return redirect(reverse('myblogs'))
    else:
        return redirect(reverse('base'))


def home(request):
    
    return render(request, 'home.html')


def signup(request: HttpRequest):
    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            username_availble =form.cleaned_data['username']
            user_exists = User.objects.filter(username=username_availble).exists()
            if user_exists:
                return HttpResponse("Username already exists, please. change your Username")
                
            else:
                username = form.cleaned_data['username']
                password1 = form.cleaned_data['password']
                fullname1 = form.cleaned_data['fullname']
                User.objects.create(username=username,password= password1,fullname=fullname1)
                return redirect('signin')   
        else:
            print(form.errors)
            return HttpResponse("Not Valid Data" + str(form.errors))
    return render(request, 'sign_up.html')


def signin(request:HttpRequest):
  #  if request.method == 'POST':
        form = sign_in(request.POST)
        if form.is_valid():
            username1 = form.cleaned_data['username']
            user1 = User.objects.get(username=username1)
            if user1:
                return redirect('myblogs')
            else:
                return HttpResponse("User Not Found")
        else:
                print(form.errors)
                return HttpResponse("Not Valid Data" + str(form.errors))
   
   # return render(request, 'sign_in.html')

@login_required
def show_my_blogs(request):
    return render(request, 'my_blog.html')

