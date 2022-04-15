<template>
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
                <router-link to="/user-preferences" class="nav-link">Preferences</router-link>
                <router-link to="/playlists" class="nav-link">Playlists</router-link>
                <router-link to="/About" class="nav-item nav-link">About</router-link>
                <router-link to="/Auth" class="nav-item nav-link ml-auto">Login</router-link>
            </div>
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
