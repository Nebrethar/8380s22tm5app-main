{% extends 'Base.html' %} 
{% block body_content %}
<template>
    <div  class="text-white">
        <!-- Welcome Text -->
        <h1 class="py-sm-5 masthead-heading mb-0" ><b>You are now logged out.</b></h1>
        <p class="py-sm-5 mb-2" style="font-size: 2.25rem !important">See you again soon!</p>
    </div>
</template>

<script>

import router from '../router';
import {APIService} from '../http/APIService';
const apiService = new APIService();

export default {
  name: 'LogOut',
  mounted: function () {
    history.pushState(
        {},
        null,
        '/'
    )
  }
}
</script>
{% endblock %}