<template>
    <div>
        <!-- Welcome Text -->
        <h1><b>Welcome User!</b></h1>
        <a @click="viewCustomers" class="btn btn-primary">User Preferences</a>
        <!-- Welcome Features -->
        <div class="row align-items-center justify-content-center">
            <div class="card" style="width:1000px">
                <img :src="require('@/assets/sun-icon.png')" class="card-img-top" style="height: 10rem; width: 10rem;">
                <img :src="require('@/assets/music-icon.png')" class="float-right" style="height: 10rem; width: 10rem;"> 
                    Now Playing: Enemy x Imagine Dragons
                <h5>75&#176;</h5>
                <div class="card-body">
                    This weather calls for a sunny playlist!
                </div>
            </div>
            <div class="card-group">
                <div class="card">
                  <div class="card-body">
                    <h5 class="card-title">Your Playlists</h5>
                    <ul>
                        <li><a href="#" class="card-link">All Recommendations</a></li>
                        <li><a href="#" class="card-link">Playlist 1</a></li>
                        <li><a href="#" class="card-link">Playlist 2</a></li>
                    </ul>
                  </div>
                </div>
                <div class="card">
                  <div class="card-body">
                    <h5 class="card-title">Recommendations</h5>
                    <ul>
                        <li><a href="#" class="card-link">Weather</a></li>
                        <li><a href="#" class="card-link">Genre</a></li>
                        <li><a href="#" class="card-link">Random</a></li>
                        <li><a href="#" class="card-link">Music Videos</a></li>
                    </ul>
                  </div>
                </div>
            </div>
            <div class="card" style="width:1000px">
                <h5 class="card-title">Random Video from your Recommendations: Enemy x Imagine Dragons</h5>
                <iframe width="999" height="500" src="https://www.youtube.com/embed/D9G1VOjN_84" title="YouTube video player" 
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
        </div>
    </div>
</template>