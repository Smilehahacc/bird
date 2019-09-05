<template>
  <div id='app'>
    <Header />
    <el-menu :default-active="this.$router.path"
             router
             style="height: 60px"
             mode="horizontal"
             @select="handleSelect">
      <el-menu-item v-for="(item,i) in navList"
                    :key="i"
                    :index="item.name">
        {{ item.navItem }}
      </el-menu-item>
    </el-menu>

    <router-view />
  </div>
</template>

<script>
import Header from '@/views/main/components/Header'
export default {
  name: 'home',
  inject: ['reload'],
  data () {
    return {
      userName: 'lynn',
      userId: 1,
      isLogin: false,
      isCollapse: true,
      navList: [
        { name: '/discernCenter', navItem: '识图中心' },
        { name: '/userAssess', navItem: '用户评价' },
        { name: '/aboutTeam', navItem: '开发团队' }
      ]
    }
  },
  components: {
    Header
  },
  methods: {

  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
</style>
