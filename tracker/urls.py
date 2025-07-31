from django.urls import path
from .views import home, login,sign_up

urlpatterns = [
    path('home/',home, name='home'),
    path('',login, name = 'login'),
    path('signup/',sign_up, name = 'sign_up')
]