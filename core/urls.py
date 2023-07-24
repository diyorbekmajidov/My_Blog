from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include(('django.contrib.auth.urls', 'django.contrib.auth'), namespace='login')),
    path('register/', users_views.register, name='register'),
    
]
