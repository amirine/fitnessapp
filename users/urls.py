from django.urls import path
from .views import sayhi, RegisterUser, LoginUser

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('sayhi/', sayhi, name='sayhi'),
]
