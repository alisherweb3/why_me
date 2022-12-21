from django.urls import path
from . import views as user_profile_views


urlpatterns = [
    path('<slug:user>/', user_profile_views.user_profile_page, name='userprofilepage'),
]