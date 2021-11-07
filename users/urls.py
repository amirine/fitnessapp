from django.urls import path
from .views import RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    # path('test/login/', TestLoginUser.as_view(), name='test_login'),
    # path('test/register/', TestRegisterUser.as_view(), name='test_register'),
]
