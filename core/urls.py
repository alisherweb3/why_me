from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('space/', include('main.urls')),
    path('me/', include('user_profile.urls')),
]
