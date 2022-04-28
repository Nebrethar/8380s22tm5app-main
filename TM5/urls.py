from django.urls import include, path, re_path
from rest_framework import routers
from music import views
from django.contrib import admin
from django.urls import re_path
from django.conf.urls.static import static
from pathlib import Path
import os
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('youtube-store/', views.youtube_store),
    path('get-youtube/<artist>/<song>/', views.youtube_get),
    path('get-playlists/', views.get_playlists),
    path('facebook-post/', views.post_facebook),
    path('twitter-post/', views.post_twitter),
    path('twitter-flow/', views.flow_twitter),
    path('random-song/', views.random_song),
    path('weather-song/<int:zipcode>/', views.weather_song),
    path('signup/', views.RegisterView.as_view(), name='auth_register'),
    path('auth/', views.authentication, name='auth'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]