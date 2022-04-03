import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: false,
    token:'',
    refresh:'',
  },
  getters: {
  },
  mutations: {
    initializeStorage(state){
      if(localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        //the is authenticated state should stay false, because we don't know if the token is still valid
      }else{
        //if token doesn't exist so isAuthenticated is set to false
        state.token = ''
        state.isAuthenticated=false // we set this to false, because authentication is required if the token does not exist
      }
      if(localStorage.getItem('refresh')){
        //if refresh exists
        state.refresh = localStorage.getItem('refresh')
      }else{
        state.refresh = ''
      }
    }, 
    setToken(state, token){
      state.token = token
      console.log('token set: ', token)
    },
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
    },
    setRefresh(state, refresh){
      state.refresh = refresh
      console.log('refresh set: ', refresh)
    },
    removeRefresh(state){
      state.refresh = ''
      console.log('refresh cleared')
    },
  },
  actions: {
  },
  modules: {
  }
})
