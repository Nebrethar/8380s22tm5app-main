<template>
  <div>
    <!-- Welcome Features -->
    <div class="row align-items-center justify-content-center">
      <h1><b>Welcome {{ validUserName }}! </b><a @click="viewCustomers" class="btn btn-dark">User Preferences</a>&nbsp;</h1>
    </div>
    <br>
    <div class="row align-items-center justify-content-center">
      <h2>Your random music recommendation is:</h2>
    </div>
    <div class="row align-items-center justify-content-center">
      <h2>Song by Artist</h2>
    </div>
    <br>
    <div class="row align-items-center justify-content-center">
      <div class="card-group" style="width:900px">
        <div class="col-lg-4">
          <div class="btn py-2" id="twitterButton">Share on Twitter</div>
        </div>
        <div class="col-lg-4">
          <div class="btn py-2" id="facebookButton">Post on Facebook</div>
        </div>
        <div class="col-lg-4">
          <div class="btn btn-dark py-2" id="playlistButton">Add to your Playlist</div>
        </div>
      </div>
    </div>
    <br>
    <div class="row align-items-center justify-content-center">
      <div class="card" style="width:1000px">
        <h3 class="card-title pt-3 pb-1" style="color: black">Music Video: Enemy x Imagine Dragons</h3>
        <iframe width="975" height="500" src="https://www.youtube.com/embed/D9G1VOjN_84" title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
    </div>
  </div>
</template>

<script>
import router from '../router';
import {APIService} from '../http/APIService';
const apiService = new APIService();

export default {
  name: "Random",
  data: () => ({
    validUserName: "Guest",
    recommendation: [],
  }),
  mounted() {
    this.getRecommendation();
  },
  methods: {
    getRecommendation() {
      if (localStorage.getItem("isAuthenticates")
          && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {
        this.validUserName = JSON.parse(localStorage.getItem("log_user"));
      }
    },
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