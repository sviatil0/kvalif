"""WAD URL Configuration

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
from django.urls import path
from pages.views import delete_view
from pages.views import add_view
from pages.views import show_view
from pages.views import update_view
from pages.views import delete_view
from pages.views import turn_on_view
from pages.views import turn_off_view
from rest_framework.urlpatterns import format_suffix_patterns
from esp32 import views
urlpatterns = [
     path('admin/', admin.site.urls),
     path('add/',add_view, name='add'),
     path('',show_view, name='show'),
     path('esp32/',views.EspList.as_view()),
     path('update/<int:id>',update_view,name="update"),
     path('delete/<int:id>',delete_view,name="delete"),
     path('turn_on/<int:id>',turn_on_view,name="turn_on"),
     path('turn_off/<int:id>',turn_off_view,name="turn_off"),

]

urlpatterns = format_suffix_patterns(urlpatterns)