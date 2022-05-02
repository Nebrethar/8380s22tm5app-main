<template>
  <div>
    <!-- Welcome Features -->
    <div class="row align-items-center justify-content-center">
      <h1><b>Welcome {{ validUserName }}! </b></h1>
    </div>
    <br>
    <div v-if="this.weather == 'Clear'" class="row align-items-center justify-content-center">
      <h2>Clear skies call for:</h2>
    </div>
    <div v-else-if="this.weather == 'Thunderstorm'" class="row align-items-center justify-content-center">
      <h2>This storm brewed up:</h2>
    </div>
    <div v-else-if="this.weather == 'Drizzle'" class="row align-items-center justify-content-center">
      <h2>Save this for a rainy day:</h2>
    </div>
    <div v-else-if="this.weather == 'Snow'" class="row align-items-center justify-content-center">
      <h2>When the weather outside is frightful:</h2>
    </div>
    <div v-else-if="this.weather == 'Clouds'" class="row align-items-center justify-content-center">
      <h2>Music for a cloudy day:</h2>
    </div>
    <div v-else-if="this.weather == 'Mist'" class="row align-items-center justify-content-center">
      <h2>Music in the mist:</h2>
    </div>
    <div class="row align-items-center justify-content-center">
      <h2>{{ song }} by {{ artist }}</h2>
    </div>
    <br>
    <div class="row align-items-center justify-content-center">
      <div class="card-group" style="width:900px">
        <div class="col-lg-4">
          <a class="btn py-2" id="twitterButton" href="https://8380s22tm5app.com/twitter-post/">Share on Twitter</a>
        </div>
        <div class="col-lg-4" style="visibility:hidden">
          <div class="btn py-2" id="facebookButton">Post on Facebook</div>
        </div>
        <div class="col-lg-4">
          <a class="btn btn-dark py-2" id="facebookButton" href="https://8380s22tm5app.com/facebook-post/">Post on Facebook</a>
        </div>
      </div>
    </div>
    <br>
    <div class="row align-items-center justify-content-center">
      <div class="card" style="width:1000px">
        <iframe id="musicVideo" width="975" height="500" style="padding:20px 20px 20px 20px" src=""
                title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
                encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
        </iframe>
      </div>
    </div>
  </div>
</template>

<script>
import router from '../router';
import {APIService} from '../http/APIService';
const apiService = new APIService();

export default {
  name: "Weather",
  data: () => ({
    validUserName: "Guest",
    weather: "",
    youtubeID: "",
    song: "",
    artist: "",
  }),
  methods: {
    getRecommendation() {
      apiService.getWeather("68124").then(response => {
        this.weather = response.data.weather;
        this.youtubeID = response.data.youtube.split("=")[1];
        this.song = response.data.tracks.items[0].name;
        this.artist = response.data.tracks.items[0].album.artists[0].name;
        document.getElementById("musicVideo").src = "https://www.youtube.com/embed/" + this.youtubeID;
        if (localStorage.getItem("isAuthenticates")
            && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {
          this.validUserName = JSON.parse(localStorage.getItem("log_user"));
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
  },
  mounted: function () {
    this.getRecommendation();
    history.pushState(
        {},
        null,
        '/'
    );
  }
};
</script>

<style>
#twitterButton {
  background-color: #1DA1F2;
  color: white;
  box-shadow: 0 1px 0 grey, 0 5px 0 whitesmoke, 0 6px 6px grey;
}
#facebookButton {
  background-color: #3b5998;
  color: white;
  box-shadow: 0 1px 0 grey, 0 5px 0 whitesmoke, 0 6px 6px grey;
}
#playlistButton {
  color: white;
  box-shadow: 0 1px 0 grey, 0 5px 0 whitesmoke, 0 6px 6px grey;
}
</style>