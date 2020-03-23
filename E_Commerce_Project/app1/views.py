from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    if request.method == 'POST':
        uname = request.POST["username"]
        password = request.POST["pass"]
        user = auth.authenticate(username=uname, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, "home.html")
        else:
            return render(request, "index.html", {'wrong': "Username or password is wrong!"})
    else:
        return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        uname = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        re_password = request.POST["re_password"]

        if User.objects.filter(username=uname).exists():
            return render(request, "register.html", {'user_name_taken': 'Username already taken!'})
        elif User.objects.filter(email=email).exists():
            return render(request, "register.html", {'email_taken': 'Email already registered!'})
        elif password != re_password:
            return render(request, "register.html", {'password_mismatch': 'Password not matching!'})
        elif 'agree_term' not in request.POST:
            return render(request, "register.html", {'not_agree': 'Please accept the Terms of Service!'})
        else:
            user = User.objects.create_user(username=uname, password=password, email=email)
            user.save()
            messages.info(request, "Successfully registered!")
            return render(request, "index.html")
    else:
        return render(request, "register.html")


def home(request):
    return render(request, "home.html")



