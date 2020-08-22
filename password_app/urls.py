from django.conf.urls import url
from django.urls import path
from password_app import views


app_name = 'password_app'

urlpatterns = [
    path('register/',views.register,name= 'registered'),
    path('user_login', views.user_login, name='user_login'),
]
