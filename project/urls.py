"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^user_login/', views.user_login, name="user_login"),
    url(r'^menu$', views.menu, name="menu"),
    url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^mess/$', views.mess, name="mess"),
    url(r'^breakfast/$', views.breakfast, name="breakfast"),
    url(r'^lunch/$', views.lunch, name="lunch"),
    url(r'^dinner/$', views.dinner, name="dinner"),
    url(r'^restaurant/$', views.restaurant, name="restaurant"),
    url(r'^rbreakfast/$', views.rbreakfast, name="rbreakfast"),
    url(r'^rlunch/$', views.rlunch, name="rlunch"),
    url(r'^rdinner/$', views.rdinner, name="rdinner"),
]
