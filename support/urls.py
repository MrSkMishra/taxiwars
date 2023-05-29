from django.urls import path
from .views import getting_views,login_page,landing_page,sign_up_view,VerifyDriverAPIView,GetVerifiedAPIView,getting_customer_details

# home,
urlpatterns = [
    path('myview1/', getting_views, name='myview'),
    # path('home/', home, name='home'),
    path('login/',login_page , name='login'),
    path('', landing_page,name="landing_page"),
    path('signupurl', sign_up_view,name="signup"),
     path('api/driver/verify/<int:driver_id>/', VerifyDriverAPIView.as_view(), name='verify_driver'),
    path('api/driver/get/', GetVerifiedAPIView.as_view(), name='driver-get'),
    path('customerview/', getting_customer_details, name='customerview'),

]