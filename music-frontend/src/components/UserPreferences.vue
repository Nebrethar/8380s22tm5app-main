{% extends 'Base.html' %} 
{% block body_content %}
<template>
    <div  class="text-white">
        <!-- Welcome Text -->
        <h1 class="py-sm-5 masthead-heading mb-0" ><b>User Preferences</b></h1>
    </div>
</template>

<script>

import router from '../router';
import {APIService} from '../http/APIService';
const apiService = new APIService();

export default {
  name: 'UserPreferences',
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