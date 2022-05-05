{% extends 'Base.html' %} 
{% block body_content %}
<template>

  <div class="container">
    <div class="row align-items-center justify-content-center">
      <div class="col-lg-5">
        <div class="card mx-auto shadow">
          <div class="card-body">
            <div class="card-title text-black" style="text-align:left;font-weight:bold;"><span>User Preferences</span></div>
            <div class="card-text pt-2">

              <form>
                <div class="form-group my-2">
                  <div class="card-title text-black" style="text-align:left;"><span>First Name:</span></div>
                  <input
                      id="firstName" type="text" class="form-control" placeholder="First Name" v-model="userPreferences.first_name">
                </div>
                <div class="form-group my-2">
                  <div class="card-title text-black" style="text-align:left;"><span>Last Name:</span></div>
                  <input id="lastName" type="text" class="form-control" placeholder="Last Name" v-model="userPreferences.last_name">
                </div>
                <div class="form-group my-2">
                  <div class="card-title text-black" style="text-align:left;"><span>Email:</span></div>
                  <input id="email" type="email" class="form-control" placeholder="Email Address" v-model="userPreferences.email">
                </div>
                <div class="form-group my-2">
                  <div class="card-title text-black" style="text-align:left;"><span>Username:</span></div>
                  <input id="username" type="username" class="form-control" placeholder="Username" v-model="userPreferences.username">
                </div>
                <!--
                <div class="form-group my-2">
                  <div class="card-title text-black" style="text-align:left;"><span>Confirm password to save:</span></div>
                  <input id="password" type="password" class="form-control" placeholder="Password" v-model="credentials.password">
                </div>
                <div
                    v-if="authenticate === false"
                    close-icon="mdi-close-circle"
                    :value="true"
                    class="alert alert-danger"
                    role="alert"
                    dense
                >
                  Password is incorrect. Please Try again.
                </div>
                -->

                <button type="submit" class="btn btn-primary my-2" @click="onSubmit">Submit</button>
              </form>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>

import router from '../router';
import {APIService} from '../http/APIService';
const apiService = new APIService();

export default {
  name: 'UserPreferences',
  data () {
    return {
      userPreferences: {},
    }
  },
  methods: {
    getUserPreferences() {
      apiService.getUser(JSON.parse(localStorage.getItem("log_user"))).then(response => {
        this.userPreferences = response.data;
      })
    },
    onSubmit: function() {
      console.log("PREFS")
      console.log(this.userPreferences);
      apiService.updateUser(this.userPreferences);
    }
  },
  mounted: function () {
    history.pushState(
        {},
        null,
        '/'
    );
    this.getUserPreferences();
  }
}
</script>
{% endblock %}