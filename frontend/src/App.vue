<template>

    <button v-if="!this.$store.state.isAuthenticated" @click="login()" type="button" >
        <span>login</span>
    </button>      
    <button v-else @click="logout()">
        <span> logout</span>
    </button>

  <router-view/>
</template>

<script>
import axios from 'axios'
export default {
  beforeCreate(){
    this.$store.commit('initializeStorage')
  },
  created(){
    this.verifyAccess()
  },
  methods:{
    async verifyAccess(){
        const token = this.$store.state.token
        await axios.post('/auth/token/verify/', {"token":token})
        .then(response=>{
            console.log('access is valid')
            this.$store.state.isAuthenticated = true
            this.$router.push('/')
        })
        .catch(err=>{
            console.log(err)
            console.log('access not valid')
            this.$store.isAuthenticated = false
        })
    },
    async login(){
      const refresh = this.$store.state.refresh
      if(typeof refresh === 'undefined'){
        console.log('refresh undefined')
        this.$router.push('/login')
      }
      else{
        const data={
          'refresh': refresh
        }
        console.log('inside else, refresh exists')
        await axios.post('/auth/token/refresh/', data)
        .then(response=>{
          console.log(response.data)
          const token = response.data.access
          this.$store.commit('setToken', token) //setting the access token
          this.$store.commit('setRefresh', refresh) //setting the refresh token
          localStorage.setItem('token', token) //storing the access token to the localstorage, so that the user won't have to repeat everything if he/she reloads the page
          localStorage.setItem('refresh', refresh) //storing the refresh token to the localstorage, so that the user won't have to repeat everything if he/she reloads the page
          this.$store.isAuthenticated = true
          this.$router.push('/')
        })
        .catch(err=>{
          console.log(err)
          this.$router.push('/login')
        })
      }
    },
    logout(){
      localStorage.removeItem("token")
      this.$store.commit('removeToken')
      this.$router.push('/')
    }
  }
}
</script>


