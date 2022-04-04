<template>
    <form @submit.prevent="register">
        <!-- username input -->
        <input 
            type="text"
            v-model="email"
            placeholder="email" />
        <!-- password input -->    
        <input 
            type="password"
            v-model="password"
            placeholder="Password" />
        <!-- password2 input -->    
        <input 
            type="password"
            v-model="password2"
            placeholder="Confirm Password" />
        <!-- error message -->
        <div v-for="error in errors" v-bind:key="error" >
            <div>
                <span >{{error}}.</span>
            </div>
        </div>
        <!-- submit button -->
        <button
            type="submit"
        >Create Account</button>
    </form>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return{
            email:'',
            password:'',
            password2:'',
            errors: [],
        }
    },
    methods:{
        register(){
            this.errors = []
            if (this.email === '') {
                this.errors.push('The email is missing')
            }
            if (this.password === '') {
                this.errors.push('The password is missing')
            }
            if (this.password !== this.password2) {
                this.errors.push('The passwords doesn\'t match')
            }
            if (!this.errors.length) {
                const formData = {
                    email: this.email,
                    password: this.password
                }
                axios
                .post("/auth/signup/", formData)// posting the data to the bacend
                .then(response => {
                    console.log(response)
                    //this.$router.push('/login') uncomment if you have a login view
                })
                .catch(error => {
                    console.log(error)
                })
            }
        }
    }
}
</script>