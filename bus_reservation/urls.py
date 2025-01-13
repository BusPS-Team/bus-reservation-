"""
URL configuration for bus_reservation project.

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
from django.urls import path
from . import views
from .views import bus_timings_redirect
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import combined_bus_data_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('bus/<int:bus_id>/', views.bus_detail, name='bus_detail'),
    path('bus_timings/', views.bus_timings_redirect, name='bus_timings_re'),
    path('bus_timings/', views.combined_bus_data_view, name='combined_bus_data'),
    path('Booknow.html/', views.book_now, name='booking')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
