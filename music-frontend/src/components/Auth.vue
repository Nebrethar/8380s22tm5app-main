<template>

  <div class="container">
    <div class="row align-items-center justify-content-center">
      <div class="col-12 col-sm-6 col-md-4 col-lg-4">
        <div class="card mx-auto shadow">
          <div class="card-body">
            <div class="card-title text-black" style="text-align:left;font-weight:bold;"><span>Login</span></div>
            <div
                v-if="showMsg === 'error'"
                close-icon="mdi-close-circle"
                :value="true"
                class="alert alert-danger"
                role="alert"
                dense
            >
              Invalid username or password. Please Try again.
            </div>
            <div class="card-text pt-2">
              <div class="col-md-10 mb-3">
                <div class="input-group">
                  <div class="input-group-prepend">
                    <span class="input-group-text">@</span>
                  </div>
                  <input
                      v-model="credentials.username"
                      :counter="70"
                      label="Username"
                      :rules="rules.username"
                      maxlength="70"
                      required
                      type="text"
                      class="form-control mb-3"
                      placeholder="Username"
                      aria-describedby="inputGroupPrepend2"
                  />

                  <div class="w-100"></div>

                  <div class="input-group-prepend">
                    <span class="input-group-text">***</span>
                  </div>
                  <input
                      :type="showPassword ? 'text' : 'Password'"
                      v-model="credentials.password"
                      label="Password"
                      :rules="rules.password"
                      maxlength="20"
                      required
                      :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                      @click:append="showPassword = ! showPassword"
                      class="form-control"
                      placeholder="Password"
                      aria-describedby="inputGroupPrepend2"
                      type="submit"
                  />
                </div>
              </div>

              <router-link to="/Signup"  class="btn btn-secondary mx-2" ref="Signup">Sign Up</router-link>
              <button type="submit" ref="form" @click.prevent="login" class="btn btn-primary mx-2">Login</button>

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
  name: 'Auth',

  data: () => ({
    credentials: {},
    valid: true,
    showMsg: '',
    loading: false,
    rules: {
      username: [
        v => !!v || "Username is required",
        v => (v && v.length > 3) || "A username must be more than 3 characters long",
        v => /^[a-z0-9_]+$/.test(v) || "A username can only contain letters and digits"
      ],
      password: [
        v => !!v || "Password is required",
        v => (v && v.length > 7) || "The password must be longer than 7 characters"
      ]
    },
    showPassword: false,
  }),
  methods: {
    sleep(ms) {
        return new Promise((resolve) => {
        setTimeout(resolve, ms);
      });
    },
    login() {
      // checking if the input is valid
      if (this.$refs.form) {
        this.loading = true;
        apiService.authenticateLogin(this.credentials).then((res)=>{
          localStorage.setItem('token', res.data.access);
          localStorage.setItem('isAuthenticates', true);
          localStorage.setItem('log_user', JSON.stringify(this.credentials.username));
          //router.push("/");
          //router.go(-1);
          console.log(router.resolve("Authin").fullPath)
          window.location.href = "https://stately-granita-d9d023.netlify.app/" + router.resolve("Authin").fullPath
          //router.push("Authin").then(window.location.reload())
          //this.sleep(30)
          console.log("done")
          this.$forceUpdate();
        }).catch(e => {
          this.loading = false;
          localStorage.removeItem('isAuthenticates');
          localStorage.removeItem('log_user');
          localStorage.removeItem('token');
          // router.go(-1);
          this.showMsg = 'error';
        })
      }
    }
  }
}
</script>

<style>

input {
  padding: 1em
}

form {
  display: flex;
  justify-content: center;
  flex-direction: column;
}


</style>
