from django.contrib import admin
from django.urls import path, include
from AdminApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AdminApp.urls')),
]
