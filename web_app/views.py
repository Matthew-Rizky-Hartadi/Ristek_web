from django.shortcuts import render, redirect
from .models import Post
import datetime
from django.db import transaction

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

# Create your views here.
def show_home(request):
    Posts = Post.objects.all()
    Posts.reverse()
    print(Posts)
    context= {
        'user': request.user,
        'posts': Posts,
    }
    return render(request, "home.html", context)

def show_profile(request):
    Posts = Post.objects.filter(user = request.user)
    
    return render(request, "profile.html")

def non_user_home(request):
    Posts = Post.objects.all()
    print(Posts)
    context= {
        'posts' : Posts,
    }
    return render(request, "non_user_home.html", context)

def register(request):
    form= UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Axcount successfully created!')
            return redirect('web_app:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("web_app:show_home")) # create response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return redirect('web_app:show_home')
            
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def add_post(request):

    if request.method == "POST":
        post = request.POST.get('content')
        if post != "" and request.user != None:
            print(f"Adding post with content '{post}' and user {request.user.username}")
            data = Post.objects.create(user=request.user, date=datetime.datetime.today(),content=post)
            print(f"Post added with id {data.id}")
            return JsonResponse({
                    "pk": data.id,
                    "fields": {
                        "user": data.user.username,
                        "content": data.content,
                        "date": data.date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    },
                },
                status=200,
            )
        else:
            messages.info(request, "Please add a post")

def add_post2(request):

    if request.method == "POST":
        post = request.POST.get('post')
        if post != "" and request.user != None:
            Post.objects.create(user=request.user, date=datetime.datetime.today(),content=post)
        elif request.user == None:
            Post.objects.create(date=datetime.datetime.today(),content=post)
        else:
            messages.info(request, "Please add a post")
    
    return render(request, 'non_user_home.html')

def show_data_json(request):
    data = Post.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")