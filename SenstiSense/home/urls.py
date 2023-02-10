"""SenstiSense URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

handler404 = views.custom_404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='HOME'),
    path('text',views.text,name='text'),
    path('login',views.login_user,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout_user,name='logout')
 
]
