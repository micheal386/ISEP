"""pltf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
import isep.views as bv


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', bv.func_home, name='home'),
	url(r'^OTP/$', bv.func_OTP),
    #url(r'^OTP/Result', bv.func_OTP_Result),
	url(r'^CAS/$', bv.func_Cas),
	url(r'^CAS/Result$', bv.func_Cas_Result),


]
