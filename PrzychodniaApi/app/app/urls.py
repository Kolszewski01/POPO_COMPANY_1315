"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from .views import home


from patient.views import register_patient

from user.views import CustomLogoutView, CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('', home, name='home'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register_patient/', register_patient, name='register_patient'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('kalendarz/', include('kalendarz.urls')),
]
