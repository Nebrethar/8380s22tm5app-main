<template>
<html>
<head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Music App</title>
        <!-- Favicon-->
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <!-- Font Awesome icons (free version)-->
        <!-- Google fonts-->
        <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css" />
        <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css" />
        <!-- Core theme CSS (includes Bootstrap)-->
</head>
<div>
<body id="page-top">
  <header class="masthead bg-primary text-white text-center">
    <div id="nav container d-flex align-items-center flex-column">
      <nav class="navbar text-white navbar-expand-lg bg-secondary fixed-top" style="padding-left:0.5rem;background-color: black;font-weight:bold;">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <div class="navbar-nav mr-auto">
                <router-link to="/" class="nav-item nav-link">Home</router-link>
                <router-link v-if="this.tair=='true'" to="/history" class="nav-link">History</router-link>
                <router-link v-if="this.tair=='true'" to="/user-preferences" class="nav-link">User: {{ this.useru }}</router-link>
                <!--<router-link to="/About" class="nav-item nav-link">About</router-link>-->
            </div>
        </div>
        <!--
        <div v-if="isAuthenticates">
        </div>
        <div v-else>
        </div>
  
        <router-link @click="checkLog()" tyle="float:right" to="/" class="nav-item nav-link ml-auto">Check</router-link>
        
        <router-link tyle="float:right" to="" class="nav-item nav-link ml-auto">
          {{ this.tair }}
        </router-link>
        <router-link @click="checkLog()" tyle="float:right" to="" class="nav-item nav-link ml-auto">CheckDB</router-link>
        -->
        <div v-if="this.tair=='true'">
          <!-- <router-link style="float:right" to="/user-preferences" class="nav-item nav-link ml-auto">Welcome {{this.useru}}!</router-link> -->
          <router-link @click="logout()" style="float:right" to="/logout" class="nav-item nav-link ml-auto">Logout</router-link>
        </div>
        <div v-else>
          <router-link @click="login()" tyle="float:right" to="/Auth" class="nav-item nav-link ml-auto">Login</router-link>
        </div>
      </nav>
    </div>
    <router-view/>
  </header>
    <div class="footer">
    <strong><p>Share&nbsp; 
        <img :src="require('@/static/assets/twitter.svg')" style="height: 1rem; width: 1rem;">&nbsp;
        <img :src="require('@/static/assets/facebook.svg')" style="height: 1rem; width: 1rem;"></p>
    </strong></div>
</body>
  </div>
</html>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
  text-align: center;
}

#nav a {
  font-weight: bold;
  color: #ffffff;
}

#nav a.router-link-exact-active {
  color: whitesmoke;
  background: green;
  border-radius: .5rem;
}

.footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: rgb(0, 0, 0);
  color: white;
  text-align: right;
}
</style>

<script>
import { ref } from '@vue/reactivity';
export default {
  name: 'app',
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
    login() {
      console.log("Logging in!");
    },
    logout() {
      //console.log("Logging out!");
      localStorage.setItem('token', null);
      localStorage.setItem('isAuthenticates', false);
      localStorage.setItem('log_user', null);
      //console.log("Set isAuthenticates to: " + localStorage.getItem('isAuthenticates'))
      this.checkLog()
      //this.tair=false;
    },
    checkLog() {
      //console.log("Local storage: " + localStorage.getItem('isAuthenticates'));
      this.tair = localStorage.getItem('isAuthenticates')
      this.useru = localStorage.getItem('log_user').replace(/"/g,"")
      console.log("Setting tair to: " + this.tair)
      this.$forceUpdate();
      return this.tair
    },
  },
  computed: {
    doubleCheck() {
    },
  },
  mounted: function() {
    window.addEventListener('popstate', function(event) {
      window.location.href = "/"
    });
    //console.log("Setting tair to " + localStorage.getItem('isAuthenticates'))
    var log=this.checkLog()
    //console.log("tair at render: " + log)
    this.isFetching = true;
    this.$forceUpdate();
  }
}
</script>