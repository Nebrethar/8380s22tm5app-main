{% extends 'Base.html' %} 
{% block body_content %}
<template>
    <div  class="text-white">
        <!-- Welcome Text -->
        <h1 class="py-sm-5 masthead-heading mb-0" ><b>Welcome to the Music Recommendation App!</b></h1>
        
        <!-- Welcome Features -->
        <div class="container-fluid text-black">
            <div class="row align-items-center justify-content-center">
                <div class="card-group" style="width:900px; height:200px;">
                    <div class="card" style="padding-top:18px;margin-right:0px;">
                        <img :src="require('@/static/assets/sun-icon.png')" class="mx-auto d-block" style="height: 8rem; width: 8rem;">   
                        <div class="card-body">
                            <h2 class="card-title">75&#176; Omaha, NE</h2>
                        </div>
                    </div>
                    <div class="card" style="padding-top:18px">
                        <div class="card-body">
                            <h3 class="card-title"><img :src="require('@/static/assets/music-icon.png')" style="height: 3rem; width: 3rem;"> Now Playing: Enemy x Imagine Dragons</h3>
                            The weather can help to recommend some music.
                            Login to use this feature for free!
                        </div>
                    </div>
                </div>
            </div>
            <br>
            <div class="row align-items-center justify-content-center" style="margin-top:30px">
                <div class="card" style="width:1000px">
                    <h2 class="card-title" style="padding-top:20px; padding-bottom:0px">Random Music Video: Enemy x Imagine Dragons</h2>
                    <iframe width="975" height="500" style="padding:0px 20px 20px 20px" src="https://www.youtube.com/embed/D9G1VOjN_84" title="YouTube video player" 
                    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
            </div>
        </div>
    </div>
</template>]
{% endblock %}