<template>

  <div class="container">
    <div class="row align-items-center justify-content-center">
      <div class="col-lg-5">
        <div class="card mx-auto shadow">
          <div class="card-body">
            <div class="card-title text-black" style="text-align:left;font-weight:bold;"><span>Sign Up</span></div>
            <div class="card-text pt-2">

              <form>
                <div class="form-group my-2">
                  <input id="firstName" type="text" class="form-control" placeholder="First Name" v-model="signupcreds.first_name">
                </div>
                <div class="form-group my-2">
                  <input id="lastName" type="text" class="form-control" placeholder="Last Name" v-model="signupcreds.last_name">
                </div>
                <div class="form-group my-2">
                  <input id="email" type="email" class="form-control" placeholder="Email Address" v-model="signupcreds.email">
                </div>
                <div class="form-group my-2">
                  <input id="username" type="username" class="form-control"
                         placeholder="Username" v-model="signupcreds.username"
                  >
                </div>
                <div class="form-group my-2">
                  <input id="password" type="password" class="form-control"
                         placeholder="Password" v-model="signupcreds.password"
                  >
                </div>
                <div class="form-group my-2">
                  <input id="passwordConfirm" type="password" class="form-control"
                         placeholder="Confirm Password" v-model="signupcreds.confirm"
                  >
                </div>
                <!--
                <div
                    v-if="v$.password.confirm.$error"
                    close-icon="mdi-close-circle"
                    :value="true"
                    class="alert alert-danger"
                    role="alert"
                    dense
                >
                  Password confirmation must match password.
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
import useVuelidate from '@vuelidate/core'
import { required, email, sameAs } from '@vuelidate/validators'
import {APIService} from '../http/APIService';
const apiService = new APIService();

export default {
  setup () {
    return { v$: useVuelidate() }
  },
  data () {
    return {
      signupcreds: {},
    }
  },
  validations () {
    return {
      first_name: { required },
      last_name: { required },
      email: { required, email },
      password: {
        password: { required },
        confirm: {
          required,
          //sameAsPassword: sameAs(this.password)
        },
      }
    }
  },
  methods: {
    onSubmit: function() {
      console.log("First Name: ")
      console.log(this.signupcreds)
      if (this.signupcreds.username && this.signupcreds.password && this.signupcreds.first_name && this.signupcreds.last_name && this.signupcreds.email) {
        if (this.signupcreds.password == this.signupcreds.confirm) {
          apiService.authenticateSignup(this.signupcreds).then((res)=>{
            localStorage.setItem('token', signupcreds.password);
            localStorage.setItem('isAuthenticates', true);
            localStorage.setItem('log_user', JSON.stringify(this.signupcreds.username));
            console.log("RESPONSE")
            console.log(res)
          })
          this.$router.push("/Auth")
        } else {
          alert("Passwords do not match.")
        }
      } else {
        alert("Please fill out all signup fields.")
      }
    }
  },
  mounted: function () {
    history.pushState(
        {},
        null,
        '/'
    )
  }
}
</script>

<style>

</style>