{% extends 'Base.html' %} 
{% block body_content %}
<template>
    <div  class="text-white">
        <!-- Welcome Text -->
        <h1 class="py-sm-5 masthead-heading mb-0" ><b>History</b></h1>
        <h3>Recent Recommendations for {{this.useru}}</h3>
        <table class="table table-secondary table-sm" style="width:70%; border: 1px solid black;margin-left:auto; margin-right:auto;">
          <thead>
            <tr>
              <th scope="col">Song</th>
              <th scope="col">Artist</th>
              <th scope="col">Found By</th>
              <th scope="col">Spotify Link</th>
              <th scope="col">Youtube Link</th>
            </tr>
          </thead>
            <tbody>
            <tr v-for = "song in songs" v-bind:key="song">
              <th scope="row">{{song.fields.song}}</th>
              <td>{{song.fields.artist}}</td>
              <td>{{song.fields.source}}</td>
              <td><a v-bind:href="song.fields.sf_link" target="_blank" style="color:blue">Listen on Spotify</a></td>
              <td><a v-bind:href="song.fields.yt_link" target="_blank" style="color:blue">Watch on Youtube</a></td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>

import router from '../router';
import {APIService} from '../http/APIService';
const apiService = new APIService();

export default {
  name: 'History',

  data() {
    return {
      songs: [],
      tair: true,
      useru: ""
    }
  },
  methods: {
    checkLog() {
      console.log("Local storage: " + localStorage.getItem('isAuthenticates'));
      this.tair = localStorage.getItem('isAuthenticates')
      this.useru = localStorage.getItem('log_user')//.replace(/"/g,"")
      if (this.useru.includes("\"")) {
        console.log("PULLING QUOTES")
        this.useru = this.useru.replace(/"/g,"")
      }
      console.log("tair is: " + this.tair)
      //this.$forceUpdate();
      return this.tair
    },
    getHistory() {
      apiService.getPlaylists().then(response => {
        this.songs = response.data;
      }).catch(error => {
        if (error.response.status === 401) {
          localStorage.removeItem('isAuthenticates');
          localStorage.removeItem('log_user');
          localStorage.removeItem('token');
          router.push("/auth");
        }
      });
    }
  },
  mounted: function () {
    history.pushState(
        {},
        null,
        '/'
    ),
    this.checkLog();
    this.getHistory();
  }
}
</script>
{% endblock %}