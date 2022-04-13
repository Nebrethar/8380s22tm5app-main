from django.urls import include, path, re_path
from rest_framework import routers
from django.views.generic import TemplateView
from music import views
from django.urls import re_path
from django.conf.urls.static import static
from pathlib import Path
import os

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name='index.html')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('facebook-post/', views.post_facebook),
    path('twitter-post/', views.post_twitter),
    path('random-song/', views.random_song),
    path('weather-song/<int:zipcode>/', views.weather_song),
    path('signup/', views.RegisterView.as_view(), name='auth_register'),
]