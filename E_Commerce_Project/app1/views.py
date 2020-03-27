from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Products

# Create your views here.
from django.urls import reverse



def home(request):
    products = Products.objects.all()
    return render(request, "home.html", {'products': products})


def login(request):
    if request.method == 'POST':
        uname = request.POST["username"]
        password = request.POST["pass"]
        user = auth.authenticate(username=uname, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return HttpResponseRedirect(request.path_info)
    else:
        return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        uname = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        re_password = request.POST["re_password"]

        if User.objects.filter(username=uname).exists():
            messages.info(request, "Username is already taken!")
            return HttpResponseRedirect(request.path_info)
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email is already registered!")
            return HttpResponseRedirect(request.path_info)
        elif password != re_password:
            messages.info(request, "Password not matching!")
            return HttpResponseRedirect(request.path_info)
        elif 'agree_term' not in request.POST:
            messages.info(request, "Please accept the Terms of service")
            return HttpResponseRedirect(request.path_info)
        else:
            user = User.objects.create_user(username=uname, password=password, email=email)
            user.save()
            auth.login(request, user)
            messages.info(request, "Successfully registered!")
            return redirect("/")
    else:
        return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect("/")




