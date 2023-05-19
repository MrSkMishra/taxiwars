from django.urls import path
from .views import getting_views,login_page,landing_page,sign_up_view,home
urlpatterns = [
    path('myview1/', getting_views, name='myview'),
    path('home/', home, name='home'),
    path('login/',login_page , name='login'),
    path('', landing_page,name="landing_page"),
    path('signupurl', sign_up_view,name="signup"),

]