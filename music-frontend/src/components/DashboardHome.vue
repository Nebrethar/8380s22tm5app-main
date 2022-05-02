{% extends 'Base.html' %} 
{% block body_content %}
<template>
<div>
    <!--
    <div class="row align-items-center justify-content-center">
                    <h1><b>{{ this.tair }}</b></h1><br><br>
                <div class="card-group" style="width:1250px; height:200px;">
                </div>
    </div>
    -->
    <div v-if="this.tair=='true'" class="text-white">
        <!-- Welcome Features -->
        <div class="container-fluid">
            <div class="row align-items-center justify-content-center">
                    <h1><b>Welcome {{ this.useru }}!</b></h1><br><br>
                <div v-if="this.weather == 'Clear'" class="card-group" style="width:900px; height:200px;">
                    <!--<a @click="viewCustomers" class="btn btn-dark">User Preferences</a>&nbsp;</h1>-->
                    <div class="card">
                        <div class="card-body text-black">
                            <h2 class="card-title">
                              <img :src="require('@/static/assets/sun-icon.png')" style="height: 10rem; width: 10rem;">
                              <!--&nbsp;&nbsp;75&#176;-->
                            </h2>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card-body text-black" style="padding-top:4em">
                            <h5 class="card-title">
                              <img :src="require('@/static/assets/music-icon.png')" style="height: 2rem; width: 2rem;">
                              {{ weatherSong }} x {{ weatherArtist }}
                            </h5>
                            <div>Clear skies call for some classy music.</div>
                        </div>
                    </div>
                </div>
                <div v-else-if="this.weather == 'Thunderstorm'" class="card-group" style="width:900px; height:200px;">
                  <!--<a @click="viewCustomers" class="btn btn-dark">User Preferences</a>&nbsp;</h1>-->
                    <div class="card">
                        <div class="card-body text-black">
                            <h2 class="card-title">
                                <img :src="require('@/static/assets/storm-cloud-icon.png')" style="height: 10rem; width: 10rem;">
                                <!--&nbsp;&nbsp;75&#176;-->
                            </h2>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card-body text-black" style="padding-top:4em">
                        <h5 class="card-title">
                            <img :src="require('@/static/assets/music-icon.png')" style="height: 2rem; width: 2rem;">
                            {{ weatherSong }} x {{ weatherArtist }}
                        </h5>
                      <div >Here's what the storm brewed up.</div>
                    </div>
                  </div>
                </div>
              <div v-else-if="this.weather == 'Drizzle'" class="card-group" style="width:900px; height:200px;">
                <!--<a @click="viewCustomers" class="btn btn-dark">User Preferences</a>&nbsp;</h1>-->
                <div class="card">
                  <div class="card-body text-black">
                    <h2 class="card-title">
                      <img :src="require('@/static/assets/rain-icon.png')" style="height: 10rem; width: 10rem;">
                      <!--&nbsp;&nbsp;75&#176;-->
                    </h2>
                  </div>
                </div>
                <div class="card">
                  <div class="card-body text-black" style="padding-top:4em">
                    <h5 class="card-title">
                      <img :src="require('@/static/assets/music-icon.png')" style="height: 2rem; width: 2rem;">
                      {{ weatherSong }} x {{ weatherArtist }}
                    </h5>
                    <div>Save this for a rainy day.</div>
                  </div>
                </div>
              </div>
              <div v-else-if="this.weather == 'Snow'" class="card-group" style="width:900px; height:200px;">
                <!--<a @click="viewCustomers" class="btn btn-dark">User Preferences</a>&nbsp;</h1>-->
                <div class="card">
                  <div class="card-body text-black">
                    <h2 class="card-title">
                      <img :src="require('@/static/assets/snow-icon.png')" style="height: 10rem; width: 10rem;">
                      <!--&nbsp;&nbsp;75&#176;-->
                    </h2>
                  </div>
                </div>
                <div class="card">
                  <div class="card-body text-black" style="padding-top:4em">
                    <h5 class="card-title">
                      <img :src="require('@/static/assets/music-icon.png')" style="height: 2rem; width: 2rem;">
                      {{ weatherSong }} x {{ weatherArtist }}
                    </h5>
                    <div>When the weather outside is frightful, listen to this.</div>
                  </div>
                </div>
              </div>
              <div v-else-if="this.weather == 'Clouds'" class="card-group" style="width:900px; height:200px;">
                <!--<a @click="viewCustomers" class="btn btn-dark">User Preferences</a>&nbsp;</h1>-->
                <div class="card">
                  <div class="card-body text-black">
                    <h2 class="card-title">
                      <img :src="require('@/static/assets/clouds-icon.jpeg')" style="height: 10rem; width: 10rem;">
                      <!--&nbsp;&nbsp;75&#176;-->
                    </h2>
                  </div>
                </div>
                <div class="card">
                  <div class="card-body text-black" style="padding-top:4em">
                    <h5 class="card-title">
                      <img :src="require('@/static/assets/music-icon.png')" style="height: 2rem; width: 2rem;">
                      {{ weatherSong }} x {{ weatherArtist }}
                    </h5>
                    <div>Music for a cloudy day.</div>
                  </div>
                </div>
              </div>
              <div v-else-if="this.weather == 'Mist'" class="card-group" style="width:900px; height:200px;">
                <!--<a @click="viewCustomers" class="btn btn-dark">User Preferences</a>&nbsp;</h1>-->
                <div class="card">
                  <div class="card-body text-black">
                    <h2 class="card-title">
                      <img :src="require('@/static/assets/mist-icon.jpeg')" style="height: 10rem; width: 10rem;">
                      <!--&nbsp;&nbsp;75&#176;-->
                    </h2>
                  </div>
                </div>
                <div class="card">
                  <div class="card-body text-black" style="padding-top:4em">
                    <h5 class="card-title">
                      <img :src="require('@/static/assets/music-icon.png')" style="height: 2rem; width: 2rem;">
                      {{ weatherSong }} x {{ weatherArtist }}
                    </h5>
                    <div>Music in the mist.</div>
                  </div>
                </div>
              </div>
            </div>
            <br>
            <div class="row align-items-center justify-content-center text-black">
                <div class="card-group" style="width:900px">
                    <div class="card">
                        <div class="card-header">
                            Your Playlists
                        </div>
                        <ul class="list-group list-group-flush">
                          <li class="list-group-item" style="padding-top:0.6em">
                            <router-link to="/" class="card-link">
                              <img :src="require('@/static/assets/heart-fill.svg')" style="height: 1rem; width: 1rem;">
                              <br>Recommendation<br>History
                            </router-link></li>
                        </ul>
                    </div>
                    <div class="card">
                    <div class="card-header">
                        Recommendations
                        </div>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item"><router-link to="/random" class="card-link">Random</router-link></li>
                            <li class="list-group-item"><router-link to="/weather" class="card-link">Weather</router-link></li>
                            <!--
                                <li class="list-group-item"><a href="#/genre" class="card-link">Genre</a></li>
                                <li class="list-group-item"><a href="#/random" class="card-link">Random</a></li>
                                <li class="list-group-item"><a href="#" class="card-link">Music Videos</a></li>
                            -->
                        </ul>
                    </div>
                </div>
            </div>
            <br>
            <div class="row align-items-center justify-content-center text-black">
                <div class="card" style="width:1000px">
                  <h2 class="card-title" style="padding-top:20px; padding-bottom:0px">
                    Random Music Video: {{ randomSong }} x {{ randomArtist }}
                  </h2>
                  <iframe
                      id="loggedInMusicVideo" width="975" height="500" style="padding:0px 20px 20px 20px"
                      src="" title="YouTube video player" frameborder="0"
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen>
                  </iframe>
                </div>
            </div>
        </div>
    </div>
    <div v-else class="text-white">
        <!-- Welcome Text -->
        <h1 class="py-sm-5 masthead-heading mb-0" ><b>Welcome to the <br>Music Recommendation App!</b></h1>
        
        <!-- Welcome Features -->
        <div class="container-fluid text-black">
            <div class="row align-items-center justify-content-center">
                <div class="card-group" style="width:900px; height:200px;">
                    <div class="card" style="padding-top:18px;margin-right:0px;">
                        <img :src="require('@/static/assets/sun-icon.png')" class="mx-auto d-block" style="height: 8rem; width: 8rem;">   
                        <div class="card-body">
                            <h2 class="card-title">75&#176; Omaha, NE</h2>
                        </div>
                    </div>
                    <div class="card" style="padding-top:18px">
                        <div class="card-body">
                            <h3 class="card-title"><img :src="require('@/static/assets/music-icon.png')" style="height: 3rem; width: 3rem;"> Now Playing: Enemy x Imagine Dragons</h3>
                            The weather can help to recommend some music.
                            Login to use this feature for free!
                        </div>
                    </div>
                </div>
            </div>
            <br>
            <div class="row align-items-center justify-content-center" style="margin-top:30px">
                <div class="card" style="width:1000px">
                    <h2 class="card-title" style="padding-top:20px; padding-bottom:0px">
                      Random Music Video: {{ randomSong }} x {{ randomArtist }}
                    </h2>
                    <iframe
                        id="loggedOutMusicVideo" width="975" height="500" style="padding:0px 20px 20px 20px"
                        src="" title="YouTube video player" frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen>
                    </iframe>
                </div>
            </div>
        </div>
    </div>
</div>
</template>]
{% endblock %}

<script>

import router from '../router';
import {APIService} from '../http/APIService';
const apiService = new APIService();

export default {
  name: 'DashboardHome',

  data() {
    return {
      refreshKey: false,
      auth: false,
      tair: true,
      isFetching: true,
      useru: "",
      youtubeID: "",
      randomSong: "",
      randomArtist: "",
      weatherSong: "",
      weatherArtist: "",
      weather: ""
    }
  },
  methods: {
    sleep(ms) {
        return new Promise((resolve) => {
        setTimeout(resolve, ms);
      });
    },
    checkLog() {
      console.log("Local storage: " + localStorage.getItem('isAuthenticates'));
      this.tair = localStorage.getItem('isAuthenticates')
      this.useru = localStorage.getItem('log_user').replace(/"/g,"")
      console.log("tair is: " + this.tair)
      //this.$forceUpdate();
      return this.tair
    },
    getRandomSong() {
      apiService.getRandom().then(response => {
        this.youtubeID = response.data.youtube.split("=")[1];
        this.randomSong = response.data.tracks.items[0].name;
        this.randomArtist = response.data.tracks.items[0].album.artists[0].name;
        if (localStorage.getItem("isAuthenticates")
            && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {
          document.getElementById("loggedInMusicVideo").src = "https://www.youtube.com/embed/" + this.youtubeID;
        }
        else {
          document.getElementById("loggedOutMusicVideo").src = "https://www.youtube.com/embed/" + this.youtubeID;
        }
      }).catch(error => {
        if (error.response.status === 401) {
          localStorage.removeItem('isAuthenticates');
          localStorage.removeItem('log_user');
          localStorage.removeItem('token');
          router.push("/auth");
        }
      });
    },
    getWeatherSong() {
      apiService.getWeather("68124").then(response => {
        this.weatherSong = response.data.tracks.items[0].name;
        this.weatherArtist = response.data.tracks.items[0].album.artists[0].name;
        this.weather = response.data.weather;
      }).catch(error => {
        if (error.response.status === 401) {
          localStorage.removeItem('isAuthenticates');
          localStorage.removeItem('log_user');
          localStorage.removeItem('token');
          router.push("/auth");
        }
      });
    },
  },
  computed: {
    doubleCheck() {
    },
  },
  mounted: function() {
    
    //console.log("Setting tair to " + localStorage.getItem('isAuthenticates'))
    this.checkLog()
    //console.log("tair at render: " + log)
    this.isFetching = true;
    this.$forceUpdate();
    this.getRandomSong();
    this.getWeatherSong()
  }
}
</script>
