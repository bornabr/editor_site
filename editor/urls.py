from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload_img/', views.upload_img, name='upload_img'),
    path('edit/', views.edit, name='edit')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)