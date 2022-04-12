from django.urls import include, path, re_path
from rest_framework import routers
from music import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),\
    path('twitter-post/', views.post_twitter),
    path('random-song/', views.random_song),
    path('weather-song/<int:zipcode>/', views.weather_song),
    path('signup/', views.RegisterView.as_view(), name='auth_register'),
]