"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/$', obtain_auth_token),

    url(r'^sample/', include('sample.urls', namespace='sample')),
    url(r'^ep03/', include('ep03.urls', namespace='ep03')),
    url(r'^ep04/', include('ep04.urls', namespace='ep04')),
    url(r'^ep06/', include('ep06.urls', namespace='ep06')),
    url(r'^ep08/', include('ep08.urls', namespace='ep08')),

    url(r'^api/', include('api.urls', namespace='api')),
]
