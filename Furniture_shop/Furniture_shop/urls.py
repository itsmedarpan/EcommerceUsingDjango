from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


urlpatterns = [
    path('test/', lambda request: HttpResponse('It works!')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('order/', include('order.urls')),
]
