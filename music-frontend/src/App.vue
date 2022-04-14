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
        </div>
    </div>
</nav>
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
</style>
