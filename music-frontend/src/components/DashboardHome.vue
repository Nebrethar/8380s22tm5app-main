<template>
    <div>
        <!-- Welcome Text -->
        <h1><b>Welcome to the Music Recommendation App!</b></h1>
        
        <!-- Welcome Features -->
        <div class="row align-items-center justify-content-center">
            <div class="card" style="width:1000px">
                <img :src="require('@/assets/sun-icon.png')" class="card-img-top" style="height: 10rem; width: 10rem;">
                <img :src="require('@/assets/music-icon.png')" class="float-right" style="height: 10rem; width: 10rem;"> 
                    Now Playing: Enemy x Imagine Dragons
                <h5>75&#176;</h5>
                <div class="card-body">
                    The weather can help to recommend some music.
                    Login to use this feature for free!
                </div>
            </div>
            <div class="card" style="width:1000px">
                <iframe width="999" height="500" src="https://www.youtube.com/embed/D9G1VOjN_84" title="YouTube video player" 
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
        </div>
    </div>
</template>