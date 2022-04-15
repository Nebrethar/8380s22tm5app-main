<template>
  <div id="nav">
  <nav class="container navbar navbar-expand-lg navbar-light" style="background-color: black;">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <div class="navbar-nav mr-auto">
            <router-link to="/" class="nav-item nav-link">Home</router-link>
            <router-link to="/user-preferences" class="nav-link">Preferences</router-link>
            <router-link to="/playlists" class="nav-link">Playlists</router-link>
            <router-link to="/About" class="nav-item nav-link">About</router-link>
            <router-link to="/Auth" class="nav-item nav-link ml-auto">Login</router-link>
        </div>
    </div>
</nav>
  <div class="footer">
    <p>Share&nbsp; 
      <img :src="require('@/assets/twitter.svg')" style="height: 1rem; width: 1rem;">&nbsp;
      <img :src="require('@/assets/facebook.svg')" style="height: 1rem; width: 1rem;"></p>
  </div>
 </div>
  <router-view/>
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
