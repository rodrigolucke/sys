"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.loginNoAdmin),
    path('admin/', admin.site.urls),
    #path('', include('blog.urls')),
    path('login/', views.loginNoAdmin),
    path('login/loginUser', views.loginUser),
    path('savePassagens/', views.savePassagens),
    path('index/', views.index3),
    path('teste/', views.teste),
    path('index2/', views.index, name="index"),
    path('index3/', views.index2, name="index3"),
    path('logout/', views.logoutUser),
]
