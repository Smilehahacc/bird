import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  // 定义状态
  state: {
    isLogin: false,
    userName: '',
    userId: ''
  },
  mutations: {
    setUserId (state, userId) {
      state.userId = userId
      sessionStorage.setItem('userId', userId)
    }
  },
  actions: {

  },
  getters: {
    userId: (state) => sessionStorage.getItem('userId')
  }
})

export default store
