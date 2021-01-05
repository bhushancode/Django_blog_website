from django.contrib import admin
from django.urls import path, include
from message import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.generate_, name='generate_'),
    path('profile', views.profile, name='profile'),
    path('blog', views.blog, name='blog'),
    path('login', views.login, name='login'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
