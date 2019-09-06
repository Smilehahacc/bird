<template>
  <div id='app'>
    <!-- 左侧菜单栏 -->
    <div class="left-menu">
      <el-menu :default-active="this.$router.path"
               router
               class="el-menu-vertical-demo"
               @open="handleOpen"
               @close="handleClose"
               :collapse="isCollapse">
        <el-menu-item v-for="(item,i) in navList"
                      :key="i"
                      :index="item.name"
                      @click="showMenu">
          <i :class="item.icon"></i>
          <span slot="title">{{ item.navItem }}</span>
        </el-menu-item>
      </el-menu>
    </div>

    <!-- 右侧具体操作内容 -->
    <div class="right-content">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: 'discernCenter',
  data () {
    return {
      isCollapse: true,
      navList: [
        { name: '/search', navItem: '数据爬虫', icon: 'el-icon-s-opportunity' },
        { name: '/sign', navItem: '图像标记', icon: 'el-icon-edit-outline' },
        { name: '/sort', navItem: '图像分类', icon: 'el-icon-s-data' },
        { name: '/algorithm', navItem: '算法评估', icon: 'el-icon-data-line' }
      ]
    }
  },
  components: {

  },
  methods: {
    showMenu () {
      setTimeout(() => {
        if (this.isCollapse) {
          this.isCollapse = false
          setTimeout(() => {
            this.isCollapse = true
          }, 1800)
        } else {
          this.isCollapse = true
        }
      }, 200)
    },
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  },
  created () {
    setTimeout(() => {
      this.isCollapse = false
    }, 60)
  }
}
</script>
<style>
* {
  margin: 0px;
  padding: 0px;
}
#app {
  width: 100%;
  height: auto;
}

.left-menu {
  float: left;
  width: 60px;
  max-width: 200px;
  margin: 0;
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 600px;
  margin-right: 0px;
  z-index: 999;
}
  /* 内容面板，包含爬虫、图像标记、图像分类和算法评估四大功能 */
  .right-content {
    float: left;
    width: 90%;
    min-height: 400px;
    margin: 20px 20px;
    /* background-color: #F2F6FC; */
  }
</style>
