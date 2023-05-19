from django.shortcuts import render,reverse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import requests
from django.middleware.csrf import get_token
from .models import *




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

@login_required
def home(request):
    driver = DriverDetails.objects.all()
    button_clicked = False
    context = {
        'driver':driver,
        'button_clicked':button_clicked
        }
    return render(request,'support/home.html',context)



@method_decorator(csrf_exempt, name='dispatch')
class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if any of the fields are empty
        if not username or not password:
            return Response({'error': 'Please fill in all the fields'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(username=username)
        if user.exists():
            return Response({'info': 'Username Already taken'}, status=status.HTTP_409_CONFLICT)

        user = User.objects.create(
            username=username
        )
        user.set_password(password)
        user.save()
        csrf_token = get_token(request)
        response_data = {
            'info': 'Account Created Successfully',
            'csrf_token': csrf_token,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)