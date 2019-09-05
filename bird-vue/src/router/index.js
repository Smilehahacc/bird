import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/views/login/Login'
import Home from '@/views/main/Home'
import DiscernCenter from '@/views/main/DiscernCenter'
import UserAssess from '@/views/main/UserAssess'
import AboutTeam from '@/views/main/AboutTeam'
import Search from '@/views/main/modular/Search'
import Sign from '@/views/main/modular/Sign'
import Sort from '@/views/main/modular/Sort'
import Algorithm from '@/views/main/modular/Algorithm'

Vue.use(Router)

export default new Router({
  routes: [{
    path: '/',
    name: 'login',
    component: Login
  }, {
    path: '/login',
    name: 'login',
    component: Login
  }, {
    path: '/home',
    name: 'home',
    component: Home,
    redirect: '/discernCenter',
    children: [{
      path: '/discernCenter',
      component: DiscernCenter,
      redirect: '/search',
      children: [{
        path: '/search',
        component: Search
      },
      {
        path: '/sign',
        component: Sign
      },
      {
        path: '/sort',
        component: Sort
      },
      {
        path: '/algorithm',
        component: Algorithm
      }
      ]
    },
    {
      path: '/userAssess',
      component: UserAssess
    },
    {
      path: '/aboutTeam',
      component: AboutTeam
    }
    ]
  }]
})
