from django.contrib import admin
from django.urls import path

from django.urls.conf import include
from My_Blog.views import index,table
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("ckeditor/", include('ckeditor_uploader.urls')),
    path("home/", table, name="home"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
