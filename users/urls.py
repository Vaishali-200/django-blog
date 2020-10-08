from django.contrib import admin
from django.conf.urls import url
from .views import UserSignUpAPIView
from .views import UserLoginAPIView
from .views import GetUserListView


# from .views import HelloWorld


urlpatterns = [
    # url('our_first_api', HelloWorld.as_view()),
    url('first_api', UserSignUpAPIView.as_view()),
    url('getUserList',GetUserListView.as_view()),
    url('login', UserLoginAPIView.as_view())
    ]