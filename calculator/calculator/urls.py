"""calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from operations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("add/",views.AdditionView.as_view(),name="addition"),
    path("subtract/",views.SubtractView.as_view(),name="sub"),
    path("multi/",views.MultiplicationView.as_view(),name="multi"),
    path("divide/",views.DivisionView.as_view(),name="division"),
    path("fact/",views.factorialView.as_view(),name="factorial"),
    path("prime/",views.primenumberView.as_view(),name="prime"),
    path("armstrong/",views.armstrongView.as_view(),name="armstrong"),
    path("palindrom/",views.palindromView.as_view(),name="pal"),
    path("range/",views.rangeView.as_view(),name="range"),
    path("health/",views.HealthView.as_view(),name="health"),
    path("temparature/",views.TemparatureView.as_view(),name="temp"),
    path("exponent/",views.ExponentView.as_view(),name="exponent"),
    path("login/",views.LoginView.as_view(),name="login"),
    path("registration/",views.RegistrationView.as_view(),name="register"),
    path("geo/",views.geoView.as_view(),name="geo"),
    path("location/",views.LocationView.as_view(),name="location"),
    path("",views.HomeView.as_view(),name="home"),
    
]
