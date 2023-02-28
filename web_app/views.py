from django.shortcuts import render, redirect
from .models import Post
import datetime
from django.db import transaction
import json

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.models import AnonymousUser, User

# Create your views here.
def show_home(request):
    Posts = Post.objects.all()
    User = get_user_model()
    users = User.objects.all()
    print(users)
    Posts_reversed = []
    for i in range(len(Posts)):
        index = len(Posts) - i - 1
        Posts_reversed.append(Posts[index])
    # print(Posts_reversed)
    context= {
        'user': request.user,
        'posts': Posts_reversed,
    }
    return render(request, "home.html", context)

def show_profile(request):
    Posts = Post.objects.filter(user = request.user)
    Posts_reversed = []
    for i in range(len(Posts)):
        index = len(Posts) - i - 1
        Posts_reversed.append(Posts[index])
    context= {
        'user': request.user,
        'posts': Posts_reversed,
    }
    # print(Posts_reversed)
    
    return render(request, "profile.html", context)

def non_user_home(request):
    Posts = Post.objects.all()
    User = get_user_model()
    users = User.objects.all()
    user = User.objects.get(username='anonymous')
    print(users[2])
    Posts_reversed = []
    for i in range(len(Posts)):
        index = len(Posts) - i - 1
        Posts_reversed.append(Posts[index])
    context= {
        'posts' :Posts_reversed,
        'user': user,
    }
    return render(request, "non_user_home.html", context)

def register(request):
    form= UserCreationForm()
    error = ''

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Axcount successfully created!')
            return redirect('web_app:login')
        # else:

    
    context = {
        'form':form,
        
        }
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
    print(request.method)
    print(request.POST)
    if request.method == "POST":
        post = request.POST.get('content')
        if post != "" and request.user != None:
            data = Post.objects.create(user=request.user, date=datetime.datetime.today(),content=post)
            print(type(data))
            
            # user = (User.objects.filter(pk=request.user.pk).values("username").first())
            # print(user)
            # user_dict = model_to_dict(data.user)
            # print(user_dict)
            # print(user_dict['username'])
            return JsonResponse({
                    "pk": data.id,
                    "fields": {
                        "user": 'matt',
                        "content": data.content,
                        "date": data.date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    },
                },
                status=200,
            )
        else:
            messages.info(request, "Please add a post")
    # return render(request, 'home.html')


def add_post2(request):
    print(request.user)
    if request.method == "POST":
        post = request.POST.get('content')
        print(post)
        if post != "":
            try:
                user = User.objects.get(username='anonymous')
            except User.DoesNotExist:
                user = User.objects.create_user(username='anonymous', email='anonymous@example.com', password='password')
            data = Post.objects.create(user=user,date=datetime.datetime.today(), content=post)
            return JsonResponse({
                    "pk": data.id,
                    "fields": {
                        "user": data.user,
                        "content": data.content,
                        "date": data.date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    },
                },
                status=200,
            )
        else:
            messages.info(request, "Please add a post")
    
    # return render(request, 'non_user_home.html')

def show_data_json(request):
    data = Post.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def delete_post(request, id):
    post = Post.objects.get(user = request.user, id=id)
    user_dict = model_to_dict(post.user)
    post.delete()
    return redirect('web_app:show_profile')

def logout_user(request):
    logout(request)
    return redirect('web_app:non_user_home')

def delete_A(request, id):
    post = Post.objects.get(id=id)
    print(post)
    post.delete()

    return redirect('web_app:non_user_home')

def delete_User(request, id):
    post = Post.objects.get(user = request.user, id=id)
    user_dict = model_to_dict(post.user)
    post.delete()
    return redirect('web_app:show_home')

def edit_post(request, id):
    post = Post.objects.get(user = request.user, id=id)
    print(post)

    if request.method == "POST":
        edit_post = request.POST.get('edit')

        if edit_post != "" :
            post.content = edit_post
            post.save(update_fields=["content"])
            return redirect('web_app:show_profile')
    return redirect('web_app:show_profile')
    
    

def edit_post_home(request, id):
    post = Post.objects.get(user = request.user, id=id)
    
    if request.method == "POST":
        edit_post = request.POST.get('edit')

        if edit_post != "" :
            post.content = edit_post
            post.save(update_fields=["content"])
            return redirect('web_app:show_home')

    
