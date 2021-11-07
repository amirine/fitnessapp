from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from workout import views

urlpatterns = [
    path('dashboard/', views.dashboard_page, name='dashboard'),
    path('add_training/', views.add_training_page, name='add_training'),
    path('training/<int:training_pk>/', views.training_page, name='training'),
    path('training/<int:training_pk>/exercise', views.exercise_page, name='exercise'),
    path('training/<int:training_pk>/editinfo', views.training_edit_page, name='training_edit'),
    path('training/<int:training_pk>/delete', views.training_delete_page, name='training_delete'),
    path('training/<int:training_pk>/fixinfo', views.training_fix_page, name='training_fix'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
