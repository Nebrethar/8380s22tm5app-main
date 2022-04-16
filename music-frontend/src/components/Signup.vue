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
                  <input id="firstName" type="text" class="form-control" placeholder="First Name" v-model="first_name">
                </div>
                <div class="form-group my-2">
                  <input id="lastName" type="text" class="form-control" placeholder="Last Name" v-model="last_name">
                </div>
                <div class="form-group my-2">
                  <input id="email" type="email" class="form-control" placeholder="Email Address" v-model="email">
                </div>
                <div class="form-group my-2">
                  <input id="password" type="password" class="form-control"
                         placeholder="Password" v-model="password.password"
                  >
                </div>
                <div class="form-group my-2">
                  <input id="passwordConfirm" type="password" class="form-control"
                         placeholder="Confirm Password" v-model="password.confirm"
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

export default {
  setup () {
    return { v$: useVuelidate() }
  },
  data () {
    return {
      first_name: '',
      last_name: '',
      email: '',
      password: {
        password: '',
        confirm: '',
      }
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
      this.v$.$touch();
      if (!this.v$.$error) return;
      alert('All fields are required')
    }
  }
}
</script>

<style>

</style>