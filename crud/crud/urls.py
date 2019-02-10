"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.conf import settings
from vehicles import views
'''
# [...]
urlpatterns=[
url(r'^admin/', include(admin.site.urls))
]


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles/', TemplateView.as_view(template_name="vehicles/main.html"), name='vehicle_main'),
    path('vehicles/list', views.VehicleList.as_view(), name='vehicle_list'),
    path('vehicles/create', views.VehicleCreate.as_view(), name='vehicle_create'),
    path('vehicles/update/<int:pk>', views.VehicleUpdate.as_view(), name='vehicle_update'),
    path('vehicles/delete/<int:pk>', views.VehicleDelete.as_view(), name='vehicle_delete'),
    path('vehicles/<int:pk>', views.VehicleDetail.as_view(), name='vehicle_detail'),
]
