from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, RegisterSerializer
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import authentication
from rest_framework import exceptions
import requests
import json
import os
import sys
import random
import string
import math
import time
import tweepy

from rest_framework.permissions import AllowAny

""" 
To be used with the Google API when the time comes

from google.auth.transport.requests import Request
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import webbrowser
"""

def makeid():
    result = ""
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    charactersLength = len(characters)
    lowercharacters = "abcdefghijklmnopqrstuvwxyz"
    lowerLength = len(lowercharacters)
    # print("**************")
    # print(math.floor(random.randint(0,1000)))
    i = 0
    # while i < length:
    result += characters[random.randint(0, charactersLength - 1)]

    swit = random.randint(0, 1)
    if swit == 0:
        result = result + "%"
    else:
        result = "%" + result + "%"
    # i += 1
    return result


def get_token_spotify(auth_url, client_id, client_secret):
    token_req_payload = {'grant_type': 'client_credentials'}

    token_response = requests.post(auth_url,
                                   data=token_req_payload, allow_redirects=False,
                                   auth=(client_id, client_secret))

    return token_response

def post_twitter(request):
    client = tweepy.OAuth1UserHandler(
        os.getenv('twitter_consumer_key'), os.getenv('twitter_consumer_secret'),
        callback = "https://8380s22tm5app.com/"
    )
    #URI = {}
    return redirect(client.get_authorization_url(signin_with_twitter=True))

def post_facebook(request):
    return redirect("https://www.facebook.com/v13.0/dialog/oauth?client_id=" + os.getenv('fb_client_id') + "&redirect_uri=https%3A%2F%2F8380s22tm5app.com%2F&state={\"{st=state123abc,ds=123456789}\"})")

def random_song(request):
    random_seed = makeid()
    random_offset = random.randint(0, 1000)

    spotify_token_raw = get_token_spotify('https://accounts.spotify.com/api/token', os.getenv('spotify_client_id'),
                                          os.getenv('spotify_client_secret'))
    # print(json.loads(spotify_token_raw.text)["access_token"])
    spotify_token = json.loads(spotify_token_raw.text)["access_token"]
    query = "https://api.spotify.com/v1/search?type=track&limit=1&offset=" + str(random_offset) + "&q=" + str(
        random_seed)
    uriQ = requests.get(query, headers={'Authorization': 'Bearer ' + spotify_token})
    URI = uriQ.json()
    request.session['last_random_track'] = URI['tracks']['items'][0]['name']
    request.session['last_random_artist'] = URI['tracks']['items'][0]['artists'][0]['name']
    request.session['last_random_URL'] = URI['tracks']['items'][0]['external_urls']['spotify']
    return JsonResponse(URI)


def weather_song(request, zipcode):
    weather = requests.get(
        "http://api.openweathermap.org/data/2.5/forecast?zip=" + str(zipcode) + "&appid=" + os.getenv('weather_token'))

    weatherStatus = weather.json()['list'][0]['weather'][0]['main']

    genre = "soul"
    #print(weatherStatus)
    if weatherStatus == "Clear":
        genre = "classical"
    elif weatherStatus == "Thunderstorm":
        genre = "nu metal"
    elif weatherStatus == "Drizzle":
        genre = "lo-fi chill"
    elif weatherStatus == "Rain":
        genre = "indiecoustica"
    elif weatherStatus == "Snow":
        genre = "indie folk"
    elif weatherStatus == "Clouds":
        genre = "britpop"
    elif weatherStatus == "Mist":
        genre = "pop rock"

    random_seed = makeid()
    random_offset = random.randint(0, 1000)

    spotify_token_raw = get_token_spotify('https://accounts.spotify.com/api/token', os.getenv('spotify_client_id'),
                                          os.getenv('spotify_client_secret'))
    # print(json.loads(spotify_token_raw.text)["access_token"])
    spotify_token = json.loads(spotify_token_raw.text)["access_token"]
    query = "https://api.spotify.com/v1/search?type=track&limit=1&offset=" + str(
        random_offset) + "&q=genre:\"" + "lo-fi chill" + "\""
    uriQ = requests.get(query, headers={'Authorization': 'Bearer ' + spotify_token})
    URI = uriQ.json()
    resp = {}
    status = {
        "weather": weatherStatus,
        "genre": genre
    }
    resp.update(status)
    resp.update(URI)
    request.session['last_weather_track'] = URI['tracks']['items'][0]['name']
    request.session['last_weather_artist'] = URI['tracks']['items'][0]['artists'][0]['name']
    request.session['last_weather_URL'] = URI['tracks']['items'][0]['external_urls']['spotify']
    return JsonResponse(resp)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def authentication(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)