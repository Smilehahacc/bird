// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import iView from 'iview'
import Axios from 'axios'
import qs from 'qs'
import 'iview/dist/styles/iview.css'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Vuex from 'vuex'
import store from './vuex/store'
import animate from 'animate.css'

Vue.use(Vuex)
Vue.use(ElementUI)
Vue.use(iView)
Vue.use(animate)

// 定义axios API的引用方式
Vue.prototype.$axios = Axios

// 全局axios默认值，即域名配置，减少后面请求时url的代码量，可在此统一配置
Axios.defaults.baseURL = 'http://127.0.0.1:8000'
// 配置请求参数的默认数据结构（这边为json字符串形式）
Axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
Axios.defaults.withCredentials = true

// 添加请求拦截器（可以在请求发送前对部分参数进行处理）
Axios.interceptors.request.use(function (config) {
  // 在发送请求之前做些什么
  if (config.method === 'post') {
    config.data = qs.stringify(config.data)
  }
  return config
}, function (error) {
  // 对请求错误做些什么
  return Promise.reject(error)
})

// 添加响应拦截器
Axios.interceptors.response.use(function (response) {
  // 对响应数据做点什么
  return response
}, function (error) {
  // 对响应错误做点什么
  return Promise.reject(error)
})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
