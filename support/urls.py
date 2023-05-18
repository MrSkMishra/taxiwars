from django.urls import path
from .views import getting_views,login_page,landing_page,home
urlpatterns = [
    path('myview1/', getting_views, name='myview'),
    path('login/',login_page , name='login'),
    path('', landing_page,name="landing_page"),
    path('home', home,name="home"),
]