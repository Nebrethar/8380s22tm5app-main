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
    <div v-if="this.tair=='true'">
        <!-- Welcome Features -->
        <div class="container-fluid text-black">
            <div class="row align-items-center justify-content-center">
                    <h1><b>Welcome User! </b></h1><br><br>
                <div class="card-group" style="width:1250px; height:200px;">
                    <!--<a @click="viewCustomers" class="btn btn-dark">User Preferences</a>&nbsp;</h1>-->
                    <div class="card">
                        <div class="card-body">
                            <h2 class="card-title"><img :src="require('@/static/assets/sun-icon.png')" style="height: 10rem; width: 10rem;">&nbsp;&nbsp;75&#176;</h2>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title"><img :src="require('@/static/assets/music-icon.png')" style="height: 2rem; width: 2rem;"> Now Playing: Enemy x Imagine Dragons</h5>
                            This weather calls for a sunny playlist!
                        </div>
                    </div>
                </div>
            </div>
            <br>
            <div class="row align-items-center justify-content-center">
                <div class="card-group" style="width:900px">
                    <div class="card">
                        <div class="card-header">
                            Your Playlists
                        </div>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item"><img :src="require('@/static/assets/heart-fill.svg')" style="height: 1rem; width: 1rem;"> <a href="#" class="card-link">All Recommendations</a></li>
                        </ul>
                    </div>
                    <div class="card">
                    <div class="card-header">
                        Recommendations
                        </div>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item"><a href="#/weather" class="card-link">Weather</a></li>
                            <li class="list-group-item"><a href="#/genre" class="card-link">Genre</a></li>
                            <li class="list-group-item"><a href="#/random" class="card-link">Random</a></li>
                            <li class="list-group-item"><a href="#" class="card-link">Music Videos</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <br>
            <div class="row align-items-center justify-content-center">
                <div class="card" style="width:1000px">
                    <h2 class="card-title">Random Music Video: Enemy x Imagine Dragons</h2>
                    <iframe width="975" height="500" src="https://www.youtube.com/embed/D9G1VOjN_84" title="YouTube video player" 
                    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
            </div>
        </div>
    </div>
    <div v-else class="text-white">
        <!-- Welcome Text -->
        <h1 class="py-sm-5 masthead-heading mb-0" ><b>Welcome to the Music Recommendation App!</b></h1>
        
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
                    <h2 class="card-title" style="padding-top:20px; padding-bottom:0px">Random Music Video: Enemy x Imagine Dragons</h2>
                    <iframe width="975" height="500" style="padding:0px 20px 20px 20px" src="https://www.youtube.com/embed/D9G1VOjN_84" title="YouTube video player" 
                    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
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
      useru: ""
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
  },
  computed: {
    doubleCheck() {
    },
  },
  mounted: function() {
    
    //console.log("Setting tair to " + localStorage.getItem('isAuthenticates'))
    //this.checkLog()
    //console.log("tair at render: " + log)
    this.isFetching = true;
      this.$forceUpdate();
  }
}
</script>
