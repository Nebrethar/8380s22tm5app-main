<template>
    <div>
        <!-- Welcome Text -->
        
        <!-- Welcome Features -->
        <div class="row align-items-center justify-content-center">
            <div class="card-group" style="width:1250px">
                <h1><b>Welcome User! </b><a @click="viewCustomers" class="btn btn-dark">User Preferences</a>&nbsp;</h1>
                <div class="card">
                    <div class="card-body">
                        <h2 class="card-title"><img :src="require('@/assets/sun-icon.png')" style="height: 10rem; width: 10rem;">&nbsp;&nbsp;75&#176;</h2>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title"><img :src="require('@/assets/music-icon.png')" style="height: 2rem; width: 2rem;"> Now Playing: Enemy x Imagine Dragons</h5>
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
                        <li class="list-group-item"><img :src="require('@/assets/heart-fill.svg')" style="height: 1rem; width: 1rem;"> <a href="#" class="card-link">All Recommendations</a></li>
                    </ul>
                </div>
                <div class="card">
                  <div class="card-header">
                       Recommendations
                    </div>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item"><a href="#" class="card-link">Weather</a></li>
                        <li class="list-group-item"><a href="#" class="card-link">Genre</a></li>
                        <li class="list-group-item"><a href="#" class="card-link">Random</a></li>
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
</template>