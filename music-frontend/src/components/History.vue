{% extends 'Base.html' %} 
{% block body_content %}
<template>
    <div  class="text-white">
        <!-- Welcome Text -->
        <h1 class="py-sm-5 masthead-heading mb-0" ><b>History</b></h1>
        <table class="table table-sm">
            <tr>
              <th scope="col">Song</th>
              <th scope="col">Artist</th>
              <th scope="col">Found By</th>
              <th scope="col">Spotify Link</th>
              <th scope="col">Youtube Link</th>
            </tr>
            <tbody>
            <tr v-for = "song in songs" v-bind:key="song">
              <th scope="row">{{song.fields.song}}</th>
              <td>{{song.fields.artist}}</td>
              <td>{{song.fields.source}}</td>
              <td><a v-bind:href="song.fields.sf_link" style="color:blue">Listen on Spotify</a></td>
              <td><a v-bind:href="song.fields.yt_link" style="color:blue">Watch on Youtube</a></td>
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
      songs: []
    }
  },
  methods: {
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
    this.getHistory();
  }
}
</script>
{% endblock %}