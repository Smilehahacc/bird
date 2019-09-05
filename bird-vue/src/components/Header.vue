<template>
  <el-header height="52px"
             id="pageheader">
    <div id="zhihuheader">
      <div class="header-content">
        <img :src='url111'
             class="head-img"
             @click="show" />
        <div class="head-ul">
          <el-menu :default-active='1'
                   class="el-menu-demo"
                   mode="horizontal">
            <el-menu-item index="1"
                          id="el-menu-demo-li1"
                          @click="gotohomepage()">首页</el-menu-item>
            <el-menu-item index="2"
                          id="el-menu-demo-li2">发现</el-menu-item>
            <el-menu-item index="3"
                          id="el-menu-demo-li3">等你来答</el-menu-item>
          </el-menu>
        </div>
        <div class="serch-input">
          <el-input placeholder="请输入需要查询的信息"
                    v-model="searchinput"></el-input>
        </div>
        <div class="searchbutton">
          <i class="el-icon-search"></i>
        </div>
        <el-button type="primary"
                   id="question-button">提问</el-button>
        <div class="head-user">
          <div class="headerbutton1">
            <el-badge :value="3"
                      class="item"
                      type="primary">
              <el-popover placement="bottom-end"
                          width="136px"
                          trigger="click">
                <div class="pushnotification">
                  <div class="pushnotification-header">
                    <div class="pushnotification-headermenu">
                      <el-button type="primary"
                                 icon="el-icon-more"
                                 plain></el-button>
                    </div>
                    <div class="pushnotification-headermenu">
                      <el-button type="primary"
                                 icon="el-icon-s-custom"
                                 plain></el-button>
                    </div>
                    <div class="pushnotification-headermenu">
                      <el-button type="primary"
                                 icon="el-icon-view"
                                 plain></el-button>
                    </div>
                  </div>
                  <div class="pushnotification-content"></div>
                  <div class="pushnotification-bootom">

                    <el-link :underline="false"
                             class="ar-menu"
                             @click="changecolor(1)"
                             icon="el-icon-s-tools"
                             id="bootombutton">设置</el-link>
                    <el-link :underline="false"
                             class="ar-menu"
                             @click="changecolor(2)"
                             id="bootombutton">查看全部通知</el-link>

                  </div>
                </div>
                <i class="el-icon-message-solid"
                   slot="reference"></i>
              </el-popover>
            </el-badge>
          </div>
          <div class="headerbutton2">
            <el-badge :value="12"
                      class="item">
              <el-popover placement="bottom-end"
                          width="136px"
                          trigger="click">
                <div class="pushnotification">
                  <div class="pushnotification2-header">
                    <span>我的私信</span>
                  </div>
                  <div class="pushnotification-content"></div>
                  <div class="pushnotification-bootom">

                    <el-link :underline="false"
                             class="ar-menu"
                             @click="changecolor(1)"
                             icon="el-icon-edit-outline"
                             id="bootombutton">写私信</el-link>
                    <el-link :underline="false"
                             class="ar-menu"
                             @click="gotochat()"
                             id="bootombutton">查看全部私信</el-link>

                  </div>
                </div>
                <i class="el-icon-s-comment"
                   slot="reference"></i>
              </el-popover>
            </el-badge>
          </div>
          <div class="userimg">
            <el-popover placement="bottom-end"
                        width="136px"
                        trigger="click">
              <el-row class="tac">
                <el-col :span="22">
                  <el-menu default-active="1"
                           class="el-menu-vertical-demo"
                           @open="handleOpen"
                           @close="handleClose">
                    <el-menu-item index="1"
                                  @click="gotopersonpage()">
                      <i class="el-icon-user-solid"></i>
                      <span slot="title">个人中心</span>
                    </el-menu-item>
                    <el-menu-item index="2">
                      <i class="el-icon-s-tools"></i>
                      <span slot="title">设置</span>
                    </el-menu-item>
                    <el-menu-item index="3"
                                  @click="exituser()">
                      <i class="el-icon-switch-button"></i>
                      <span slot="title">退出</span>
                    </el-menu-item>
                  </el-menu>
                </el-col>
              </el-row>
              <!-- <img :src="portraitSrc"
             style="width:30px;height:30px"  /> -->
              <Avatar class='user-portrait'
                      v-bind:src='portraitSrc'
                      slot="reference" />
            </el-popover>
          </div>
        </div>
      </div>
    </div>
  </el-header>
</template>

<script>
export default {
  name: 'head',
  data () {
    return {
      isLogin: true,
      userId: '',
      userName: '',
      searchinput: '',
      userInfor: [],
      portraitSrc: '',
      url111: require('@/assets/img/zh_logo.png')
    }
  },
  methods: {
    syncUser () {
      // 获取基本信息
      this.$axios.post('/api/findByCondition', {
        name: this.userName
      }).then(data => {
        console.log('获取用户基本信息')
        this.userInfor = data.data
        // 更新头像
        console.log('获取数据sdsdsds' + this.userInfor.infor_portrait)
        this.portraitSrc = require('@/assets/img/' + this.userInfor.infor_portrait)
      })
    },
    checkImg (imgSrc) {
      if (imgSrc === null || imgSrc.length === 0) {
        return false
      } else {
        return true
      }
    },
    getCookie (cname) {
      var name = cname + '='
      var ca = document.cookie.split(';')
      console.log('正在获取cookie...')
      for (var i = 0; i < ca.length; i++) {
        var c = ca[i]
        console.log(c)
        while (c.charAt(0) === ' ') c = c.substring(1)
        if (c.indexOf(name) !== -1) {
          return c.substring(name.length, c.length)
        }
      }
      return ''
    },
    getLoginState () {
      this.isLogin = this.getCookie('isLogin')
      this.userId = this.getCookie('userId')
      this.userName = this.getCookie('userName')
      console.log('获取用户基本信息-----------')
    },
    show: function () {
      alert('点击')
    },
    gotopersonpage: function () {
      this.$router.push('/personpage')
    },
    gotohomepage: function () {
      this.$router.push('/homepage')
    },
    gotochat: function () {
      this.$router.push('/chat')
    },
    exituser: function () {
      this.$confirm('你将要退出登陆, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$message({
          type: 'success',
          message: '已退出登陆!'
        })
        this.$router.push('/login')
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消'
        })
      })
    }
  },
  created () {
    this.getLoginState()
    if (this.isLogin) {
      this.syncUser()
    }
  }
}
</script>

<style>
.pushnotification2-header {
  width: 360px;
  height: 47px;
  text-align: center;
  line-height: 47px;
  border-bottom: 1px solid #e4e4e4;
}
#pageheader {
  padding: 0px;
}
#zhihuheader {
  width: 100%;
  height: 52px;
  padding: 0px;
  margin: 0px;
  border: #1a1a1a;
  background-color: #ffffff;
  border-bottom: 1px solid #cccccc;
}
.header-content {
  width: 1032px;
  height: 52px;
  padding: 0px 16px 0px 16px;
  margin: 0 auto;
}
.head-img {
  width: 60px;
  height: 30px;
  line-height: 60px;
  margin-top: 11px;
  float: left;
}
.head-ul {
  width: 222px;
  height: 48px;
  padding: 0px;
  margin: 0px 23px 0px 23px;
  float: left;
}
.el-menu-demo {
  width: 222px;
  height: 48px;
}
#el-menu-demo-li1,
#el-menu-demo-li2 {
  width: 70px;
  height: 48px;
}
#el-menu-demo-li3 {
  width: 70px;
  height: 48px;
  padding: 0px 0px 0px 5px;
  margin-left: 5px;
}
.serch-input {
  float: left;
  width: 298px;
  height: 34px;
  outline: none;
  border: 0px;
  /* border: solid #cccccc; */
  border-radius: 3px;
  background-color: #f6f6f6;
  margin-top: 7px;
}
.serch-input input {
  width: 298px;
  height: 34px;
  outline: none;
  border: 0px;
  background: #00000000;
  color: #1a1a1a;
  float: left;
}
.searchbutton {
  width: 27px;
  height: 34px;
  cursor: pointer;
  float: left;
  margin-left: -2px;
  padding-top: 7px;
  margin-top: 7px;
  background-color: #f6f6f6;
}
#question-button {
  width: 58px;
  height: 32px;
  line-height: 30px;
  padding: 0px;
  margin: 9px 0px 0px 16px;
  float: left;
}
.head-user {
  margin-top: 10px;
  float: right;
  width: 268px;
  height: 31px;
}
.headerbutton1 {
  width: 25px;
  height: 25px;
  color: #8590a6;
  float: left;
  margin-right: 40px;
  margin-left: 100px;
}
.headerbutton2 {
  width: 25px;
  height: 25px;
  color: #8590a6;
  float: left;
  margin-right: 40px;
}
.headerbutton1 i,
.headerbutton2 i {
  padding-top: 3px;
  cursor: pointer;
  cursor: hand;
  font-size: 25px;
}
.userimg {
  cursor: pointer;
  cursor: hand;
  width: 30px;
  height: 31px;
  float: right;
}
.pushnotification {
  float: left;
  width: 360px;
  height: 439px;
  border: 1px solid #e4e4e4;
  background-color: #ffffff;
}
.pushnotification-header {
  width: 360px;
  height: 48px;
}
.pushnotification-content {
  width: 360px;
  height: 350px;
}
.pushnotification-bootom {
  width: 327px;
  height: 40px;
  float: left;
  padding: 0px 16px 0px 16px;
  border-top: 1px solid #e4e4e4;
  background-color: #ffffff;
}
.pushnotification-headermenu {
  float: left;
}
.pushnotification-headermenu button {
  width: 120px;
  height: 48px;
  font-size: 20px;
  margin: 0px;
  border: 0px;
  border-radius: 0px;
  background-color: #ffffff;
}
#bootombutton {
  width: 100px;
  height: 40px;
  float: left;
}
</style>
