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
from django.core import serializers
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import status
import requests
import urllib.parse
import json
import os
import sys
import random
import string
import math
import time
import tweepy
import urllib.parse
from pathlib import Path
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from django.conf import settings
from .models import PlaylistModel
from youtubesearchpython import *

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
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
state = None
flow = None
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_playlists(request):
    allvals = serializers.serialize("json", PlaylistModel.objects.all())
    print(allvals)
    return JsonResponse(json.loads(allvals), safe=False)

def youtube_get(request, artist, song):
    customSearch = CustomSearch(artist + " " + song, "", limit = 1)
    link = customSearch.result()['result'][0]['link']
    jsonlink = {"yt-link": link}
    return JsonResponse(jsonlink)

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
    oauth2 = tweepy.OAuth2UserHandler(
        client_id = os.getenv('twitter_client_key'),
        client_secret = os.getenv('twitter_client_secret'),
        scope="tweet.write",
        redirect_uri = "https://stately-granita-d9d023.netlify.app/"
    )
    #URI = {}
    result = oauth2.get_authorization_url()
    #print("******************")
    #print(oauth2._client.code_verifier)
    #print(dir(oauth2.state))
    #print(oauth2.state)
    #request.session["state"] = oauth2.state
    #state = oauth2.state
    #request.session["state"] = oauth2.state
    request.session["oauth2"] = oauth2._client.code_verifier
    return redirect(result)

def user_get(request, username):
    if User.objects.filter(username=username).exists():
        users = User.objects.get(username=username)
        users_ready = model_to_dict(users)
        #users_finish = json.dumps(users_ready)
        #print(users_finish)
        return JsonResponse(users_ready, safe=False)
    else:
        return JsonResponse({"Error": "Username exists"})

def user_update(request):
    username = str(request.get_full_path).split("username=",1)[1].split("&email",1)[0]
    email = str(request.get_full_path).split("email=",1)[1].split("&first_name",1)[0]
    first_name = str(request.get_full_path).split("first_name=",1)[1].split("&last_name",1)[0]
    last_name = str(request.get_full_path).split("last_name=",1)[1].split("\'",1)[0]
    print(username)
    if User.objects.filter(username=username).exists():
        ud = User.objects.get(username=username)
        ud.username = username
        ud.email = email
        ud.first_name = first_name
        ud.last_name = last_name
        ud.save()
        users_ready = model_to_dict(ud)
        #users_finish = json.dumps(users_ready)
        return JsonResponse(users_ready, safe=False)
    else:
        return JsonResponse({"Error": "Username exists"})

    """
    print(dir(result))
    access_token_t = oauth2.fetch_token(str(result))
    client = tweepy.Client(access_token_t["access_token"])
    client.consumer_key=os.getenv('twitter_consumer_key')
    client.consumer_secret=os.getenv('twitter_consumer_secret')
    print(dir(client))
    client.create_tweet(text="Testing out the auth!", user_auth=True)
    print("***************")
    print(tweepy.errors.HTTPException)
    print("***************")
    #print("***************")
    return redirect(result)
    """

"""
def flow_twitter(request):
    #print("***************")
    #print(request.get_full_path())
    state = str(request.get_full_path).split("state=",1)[1].split("&code",1)[0]
    codetest = str(request.get_full_path).split("code=",1)[1]
    
    oauth2 = tweepy.OAuth2UserHandler(
        client_id = os.getenv('twitter_client_key'),
        client_secret = os.getenv('twitter_client_secret'),
        scope="tweet.write",
        redirect_uri = "https://8380s22tm5app.com/twitter-flow/"
    )
    print("__________________")
    print(request.session["oauth2"])
    print("__________________")
    print(state)
    result = oauth2.get_authorization_url()
    #oauth2._client.code_verifier = request.session["oauth2"]
    #oauth2.code_verifier = "2"
    
    authorization_response = "https://8380s22tm5app.com?state=" + str(state) + "&code=" + str(codetest)
    print(authorization_response)
    access_token_t = oauth2.fetch_token(
        authorization_response
    )

    try:
        client = tweepy.Client(access_token_t["access_token"])
        client.consumer_key=os.getenv('twitter_consumer_key')
        client.consumer_secret=os.getenv('twitter_consumer_secret')
        print(dir(client))
        client.create_tweet(text="Testing out the auth!", user_auth=False)
        print("***************")
        print(tweepy.errors.HTTPException)
        print("***************")
    #print("***************")
    except tweepy.errors.Forbidden as e:
        print(dir(e))
        print(e.api_codes)
        print(e.api_errors)
        print(e.api_messages)
        print(e.args)
        print(e.response.text)
        #print(e.with_traceback())
    return redirect("https://stately-granita-d9d023.netlify.app/")
"""

def post_facebook(request):
    return redirect("https://www.facebook.com/v13.0/dialog/oauth?client_id=" + os.getenv('fb_client_id') + "&redirect_uri=https%3A%2F%2Fstately-granita-d9d023.netlify.app%2F&state={\"{st=state123abc,ds=123456789}\"})")

@permission_classes((IsAuthenticated, ))
def random_song(request):
    hd = str(request.headers)
    if "username" in request.get_full_path():
        username = urllib.parse.unquote(str(request.get_full_path).split("username=",1)[1].split("\'",1)[0])
    else:
        username = "instructor"
    print("USERNAME: " + username)
    if "Authorization" in hd:
        chkval = hd.split("\'Authorization\':", 1)[1]
    else:
        chkval = "Bearer"
    if "Bearer" in chkval:
        random_seed = makeid()
        random_offset = random.randint(0, 1000)

        spotify_token_raw = get_token_spotify('https://accounts.spotify.com/api/token', os.getenv('spotify_client_id'),
                                            os.getenv('spotify_client_secret'))
        spotify_token = json.loads(spotify_token_raw.text)["access_token"]
        query = "https://api.spotify.com/v1/search?type=track&limit=1&offset=" + str(random_offset) + "&q=" + str(
            random_seed)
        uriQ = requests.get(query, headers={'Authorization': 'Bearer ' + spotify_token})
        URI = uriQ.json()
        request.session['last_random_track'] = URI['tracks']['items'][0]['name']
        request.session['last_random_artist'] = URI['tracks']['items'][0]['artists'][0]['name']
        request.session['last_random_album'] = URI['tracks']['items'][0]['album']['name']
        request.session['last_random_URL'] = URI['tracks']['items'][0]['external_urls']['spotify']

        #yt = youtube_get(URI['tracks']['items'][0]['name'], URI['tracks']['items'][0]['artists'][0]['name'])
        #print(yt.text)
        customSearch = CustomSearch(request.session['last_random_artist'] + " " + request.session['last_random_track'], "", limit = 1)
        request.session['yt_link'] = customSearch.result()['result'][0]['link']
        URI.update({"youtube": request.session['yt_link']})
        #print(request.session['yt_link'])

        #print(dir(PlaylistModel))
        if "nostore=true" not in request.get_full_path():
            plst = PlaylistModel(
            playlist_name="History",
            song=request.session['last_random_track'],
            artist=request.session['last_random_artist'],
            album=request.session['last_random_album'],
            yt_link=request.session['yt_link'],
            sf_link=request.session['last_random_URL'],
            source="Random",
            username=username)
            plst.save()

        response = JsonResponse(URI)
    else:
        response = JsonResponse({"LOGIN": "You must be logged in to use this feature"})
    return response

def weather_song(request, zipcode):
    hd = str(request.headers)
    if "username" in request.get_full_path():
        username = urllib.parse.unquote(str(request.get_full_path).split("username=",1)[1].split("\'",1)[0])
    else:
        username = "instructor"
    if "Authorization" in hd:
        chkval = hd.split("\'Authorization\':", 1)[1]
    else:
        chkval = "Bearer"
    if "Bearer" in chkval:
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
        request.session['last_weather_album'] = URI['tracks']['items'][0]['album']['name']
        request.session['last_weather_URL'] = URI['tracks']['items'][0]['external_urls']['spotify']

        customSearch = CustomSearch(request.session['last_weather_artist'] + " " + request.session['last_weather_track'], "", limit = 1)
        request.session['yt_link'] = customSearch.result()['result'][0]['link']        
        resp.update({"youtube": request.session['yt_link']})

        if "nostore=true" not in request.get_full_path():
            plst = PlaylistModel(playlist_name="History",
            song=request.session['last_weather_track'],
            artist=request.session['last_weather_artist'],
            album=request.session['last_weather_album'],
            yt_link=request.session['yt_link'],
            sf_link=request.session['last_weather_URL'],
            source="Weather",
            username=username)
            plst.save()

        response = JsonResponse(resp)
    else:
        response = JsonResponse({"LOGIN": "You must be logged in to use this feature"})
    return response


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

@api_view(['GET', 'POST'])
def signup(request):
    username = str(request.get_full_path).split("username=",1)[1].split("&password",1)[0]
    password = str(request.get_full_path).split("password=",1)[1].split("&email",1)[0]
    email = str(request.get_full_path).split("email=",1)[1].split("&first_name",1)[0]
    first_name = str(request.get_full_path).split("first_name=",1)[1].split("&last_name",1)[0]
    last_name = str(request.get_full_path).split("last_name=",1)[1].split("\'",1)[0]
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name)
    return JsonResponse({})

"""
def youtube_store(request):
        # The user will get an authorization code. This code is used to get the
    # access token.
    print("IN YOUTUBE")
    print(dir(request))
    print(request.get_full_path())
    #print("***************")
    #print(str(request.get_full_path).split("state=",1)[1].split("&code",1)[0])
    #print("***************")
    #print(str(request.get_full_path).split("code=",1)[1].split("&scope",1)[0])
    #print("***************")
    
    code = str(request.get_full_path).split("code=",1)[1].split("&scope",1)[0]

    scopes = "https://www.googleapis.com/auth/youtube.readonly"
    client_secrets_file = str(Path(__file__).resolve().parent) + "/client_secret.json"
    
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        client_secrets_file, scopes)
    flow.fetch_token(code=code)

    #   You can use flow.credentials, or you can just get a requests session
    #   using flow.authorized_session.
    session = flow.authorized_session()
    print(session.get('https://www.googleapis.com/userinfo/v2/me').json())
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", credentials=flow.credentials)

    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q="surfing"
    )
    response = request.execute()

    print(response)
    return response

def youtube_get(request):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    scopes = "https://www.googleapis.com/auth/youtube.readonly"

    client_secrets_file = str(Path(__file__).resolve().parent) + "/client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        client_secrets_file, scopes)
    flow.redirect_uri="http://localhost:8000/youtube-store/"
    auth_url, state = flow.authorization_url(
    # Enable offline access so that you can refresh an access token without
    # re-prompting the user for permission. Recommended for web server apps.
    access_type='offline',
    # Enable incremental authorization. Recommended as a best practice.
    include_granted_scopes='true')
    print("FLOW TIME")
    print(flow)
    rdr = redirect(auth_url)
    #print(rdr)
    #print(rdr.get_full_path())
    return rdr
"""
