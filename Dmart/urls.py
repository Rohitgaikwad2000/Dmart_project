"""
URL configuration for Dmart project.

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
from django.urls import path,include
from app.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', all_products, name = "all_products"),
    path('add-product/', add_product, name = "add_product"),
    path('update-product/<int:id>/', update_product, name = "update_product"),
    path('expire-product/<int:id>/', expire_product, name = "expire_product"),
    path('show_expire-product/', show_expire_product, name = "show_expire_product"),
    path('restore-product/<int:id>/', restore_product, name = "restore_product"),
    path('premanantly_expire-product/<int:id>/', premanantly_expire_product, name = "premanantly_expire_product"),
    path('csv/', include('csv_upload.urls')),
]

def func(r):
    r = "Rohit"
    return r

func()

