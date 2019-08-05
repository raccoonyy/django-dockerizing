from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from api.views import api, database, message

urlpatterns = [
    path('api/', api),
    path('api/database/', database),
    path('api/message/', message),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
