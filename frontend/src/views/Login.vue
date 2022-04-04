<template>
    <form @submit.prevent="submitForm">
        <!-- username input -->
        <input 
            type="text"
            v-model="username"
            placeholder="Email or username" />
        <!-- password input -->    
        <input 
            type="password"
            v-model="password"
            placeholder="Password" />
        <!-- error message -->
        <div v-for="error in errors" v-bind:key="error" >
            <div role="alert">
                <span class="block sm:inline">{{error}}.</span>
            </div>
        </div>
        <!-- submit button -->
        <button
            type="submit"
        >Log In</button>
    </form>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return{
            username:'',
            password:'',
            errors: [],
        }
    },
    methods:{
        submitForm() {
            this.errors = []
            if (this.username === '') {
                this.errors.push('The username is missing')
            }
            if (this.password === '') {
                this.errors.push('The password is missing')
            }
            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }
                axios
                    .post("/auth/token/", formData)
                    .then(response => {
                        //getting the access and refresh token from the response
                        const token = response.data.access
                        const refresh = response.data.refresh
                        // console.log(token)
                        this.$store.commit('setToken', token) //setting the token
                        this.$store.commit('setRefresh', refresh) //setting the token
                        localStorage.setItem('token', token) //storing the token to the localstorage
                        localStorage.setItem('refresh', refresh) //storing the token to the localstorage
                        this.$router.push('/')
                    })
                    .catch(error => { //catching errors
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else {
                            this.errors.push('An error has occured, please try again.')
                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }
}
</script>