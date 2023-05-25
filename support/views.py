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
from rest_framework.parsers import JSONParser
from .serializers import *
from rest_framework.generics import CreateAPIView
from django.core.paginator import Paginator
from rest_framework import generics




def landing_page(request):
    return render(request,'landing.html')


# @login_required
# def getting_views(request):
#     return render(request,"support/index.html")


@login_required
def getting_customer_details(request):
    return render(request,"support/customerview.html")


@login_required
def getting_views(request):
    try:
        api_url = 'http://localhost:8000/api/driver/get/'
        response = requests.get(api_url)

        if response.status_code == 200:
            paginated_data = response.json()
            paginator = Paginator(paginated_data, 5)
            page_number = request.GET.get('page')
            current_page_data = paginator.get_page(page_number)

            if request.method == 'POST':
                driver_id = request.POST.get('driver_id')
                verify_url = f'http://localhost:8000/api/driver/verify/{driver_id}/'
                verify_response = requests.post(verify_url)

                if verify_response.status_code == 200:
                    # Driver verified successfully
                    return redirect('myview')
                else:
                    error_message = f"Failed to verify the driver. Status code: {verify_response.status_code}"
                    return render(request, 'error.html', {'error_message': error_message})

            context = {
                'paginated_data': current_page_data,
            }

            return render(request, 'support/index.html', context)
        else:
            error_message = f"Failed to retrieve paginated data from the API. Status code: {response.status_code}"
            return render(request, 'error.html', {'error_message': error_message})
    except requests.exceptions.RequestException as e:
        error_message = f"An error occurred while making the API request: {str(e)}"
        return render(request, 'error.html', {'error_message': error_message})






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
#     driver = DriverDetails.objects.all()
#     button_clicked = False
#     context = {
#         'driver':driver,
#         'button_clicked':button_clicked
#         }
#     return render(request,'support/home.html',context)



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


# @method_decorator(csrf_exempt, name='dispatch')
# class DriverCreate(CreateAPIView):
#     parser_classes = (JSONParser,)

#     def post(self, request):
#         data = JSONParser().parse(request)
#         id = data['id']
#         verify_name = data['verify_name']

#         driver = Driver.objects.get(id=id)
#         if driver is None:
#             return Response(status=404)
#         if driver.verified:
#             return Response(status=400)

#         driver.verified = True
#         driver.save()
#         return Response(status=200, data={'message': 'Driver has been verified'})


class VerifyDriverAPIView(APIView):
    def post(self, request, driver_id):
        try:
            instance = DriverDetails.objects.get(id=driver_id)
        except DriverDetails.DoesNotExist:
            return Response({'error': 'Invalid driver ID.'}, status=404)

        instance.verified = True
        instance.save()

        return Response({'verified': True})

class GetVerifiedAPIView(generics.ListAPIView):
        queryset = DriverDetails.objects.all()
        serializer_class = DriverSerializer