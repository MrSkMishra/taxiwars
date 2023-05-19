from django.shortcuts import render,reverse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import requests



def landing_page(request):
    return render(request,'landing.html')


@login_required
def getting_views(request):
    return render(request,"support/index.html")

def sign_up_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if any of the fields are empty
        if not first_name or not last_name or not username or not password:
            messages.error(request, 'Please fill in all the fields')
            return redirect('signup')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request,'Username Already taken')
            return redirect('signup')

        user = User.objects.create(
            first_name=first_name,
            last_name = last_name,
            username = username,

        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account Created Successfully')
        return redirect('login')
    return render(request,'signup.html')
    

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if the username and password fields are not empty
        if not username or not password:
            messages.error(request, 'Please enter both username and password')
            return redirect('login')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')
            return redirect('login')
        user = authenticate(username = username , password = password)
        if user is None:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
        else:
            login(request,user)
            return redirect('myview')
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('login')

# @login_required
# def home(request):
#     response = requests.get('https://countriesnow.space/api/v0.1/countries/population/cities').json()
#     context = {
#         'response':response
#         }
#     return render(request,'support/home.html',context)