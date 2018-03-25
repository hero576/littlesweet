"""LSsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url,include

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^site01/', include("site01.urls")),
    url(r'^site001/', include("site001.urls")),
    url(r'^site002/', include("site002.urls")),
    url(r'^site003/', include("site003.urls")),
    url(r'^site004/', include("site004.urls")),
]
