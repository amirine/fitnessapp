from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('workout.urls')),
    path('user/', include('users.urls')),
]
