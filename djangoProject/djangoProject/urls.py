
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app.views import  index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'home'),


]

urlpatterns += staticfiles_urlpatterns()