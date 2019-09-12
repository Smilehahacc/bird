<template>
  <div id='app'>
    <BackTop></BackTop>
    <div class='head'>
      <div style="width: auto"><a class='head-title'
           @click='refresh'>在线识图</a></div>
      <div style="float: left;margin: 0;"><a class='head-title1'>人工智能图像技术，轻松识别图片信息</a></div>
      <div class='user-bar'>
        <Dropdown trigger="hover"
                  style="margin-left: 20px;margin-top:52px;">
          <a href="javascript:void(0)">
            <Avatar class='user-portrait'
                    v-bind:src='portraitSrc' />
          </a>
          <DropdownMenu slot="list"
                        style="text-align:center">
            <DropdownItem v-if="!isLogin">
              <router-link to="/login"><a class='menu'>登录</a></router-link>
            </DropdownItem>
            <DropdownItem v-if="isLogin"><a class='menu'
                 @click="user">个人中心</a></DropdownItem>
            <DropdownItem v-if="isLogin"><a class='menu'
                 @click="setting">设置</a></DropdownItem>
            <DropdownItem v-if="isLogin"><a class='menu'
                 @click="logout">退出</a></DropdownItem>
          </DropdownMenu>
        </Dropdown>
      </div>

    </div>
  </div>
</template>

<script>
// 固定写法，参数的赋值
export default {
  name: 'forumHead',
  inject: ['reload'],
  data () {
    return {
      portraitSrc: '',
      portraitModifyName: '',
      portraitModifySrc: '',
      isLogin: false,
      userName: '',
      userId: '',
      drawerInformation: false,
      drawerTalk: false,
      drawerUser: false,
      drawerSetting: false,
      fansNum: -1,
      followNum: -1,
      topicNum: -1,
      userInfor: [],
      isModifyShow: false,
      nameModify: '',
      emailModify: '',
      phoneModify: '',
      autographModify: ''
    }
  },
  // 一些页面交互相关方法
  methods: {
    // 刷新页面
    refresh () {
      this.$router.push('/home')
      this.reload()
    },
    // 查找校园
    search () {
      // 根据校园名查询校园
      this.$axios.post('/api/findCollegeIdByName', {
        collegeName: this.searchText
      }).then(data => {
        console.log('获取校园id进行搜索和页面跳转')
        // 查询到结果则跳转，否则提示没有结果
        if (data.data !== -1) {
          this.reload()
          this.$Message.success('搜索成功，正在进入校园...')
          this.$store.commit('setCollegeId', data.data)
          this.$router.push('/collegeDetail')
        } else {
          this.$Message.error('抱歉，没有搜索到该校园！')
        }
      })
    },
    // 显示左侧个人信息栏的信息修改页面，更新数据
    modifyShow () {
      this.isModifyShow = true
      this.nameModify = this.userInfor.infor_name
      this.emailModify = this.userInfor.infor_email
      this.phoneModify = this.userInfor.infor_phone
      this.autographModify = this.userInfor.infor_autograph
      this.portraitModifySrc = require('@/assets/img/' + this.userInfor.infor_portrait)
    },
    // 修改成功，更新数据
    modifySuccess () {
      this.isModifyShow = false
      this.userInfor.infor_name = this.nameModify
      this.userInfor.infor_email = this.emailModify
      this.userInfor.infor_phone = this.phoneModify
      this.userInfor.infor_autograph = this.autographModify
      this.userInfor.infor_portrait = this.portraitModifySrcName
      // 更新头像，同步用户名cookie和状态参数
      this.portraitSrc = require('@/assets/img/' + this.portraitModifySrcName)
      this.userName = this.nameModify
      this.setCookie('userName', this.userName, 7)
      this.$store.state.userName = this.userName
    },
    // 头像上传成功
    uploadSuccess (event, file, fileList) {
      this.portraitModifySrcName = file.name
      this.portraitModifySrc = require('@/assets/img/' + this.portraitModifySrcName)
    },
    // 发送请求，尝试保存个人信息修改
    saveModify () {
      this.$axios.post('/api/updateUserInfor', {
        userId: this.userId,
        userName: this.nameModify,
        userEmail: this.emailModify,
        userPhone: this.phoneModify,
        userPortrait: this.portraitModifySrcName,
        userAutograph: this.autographModify
      }).then(response => {
        console.log('修改用户信息')
        if (response.data === 'SUCCESS') {
          this.$Message.success('用户信息修改成功！')
          this.modifySuccess()
        } else {
          this.$Message.error('修改失败！请检查修改的信息（用户名或手机号可能重复）')
        }
      }).catch(error => {
        console.log(error)
        this.$Message.error('请求失败！' + error.status + ',' + error.statusText)
      })
    },
    // 退出登录
    logout () {
      this.clearCookie()
      this.$Message.success('退出成功！')
      this.isLogin = false
      this.userName = ''
      this.userId = ''
      this.setLoginState()
      this.reload()
    },
    // 从Vuex更新登录状态
    getLoginState () {
      this.isLogin = this.getCookie('isLogin')
      this.userId = this.getCookie('userId')
      this.userName = this.getCookie('userName')
    },
    // 退出登录后更新登录状态
    setLoginState () {
      this.$store.state.isLogin = this.isLogin
      this.$store.state.userId = this.userId
      this.$store.state.userName = this.userName
    },
    // 同步状态，读取用户信息
    syncUser () {
      this.portraitSrc = require('@/assets/img/portrait.png')
    },
    // 设置cookie
    setCookie (cname, cvalue, exdays) {
      var d = new Date()
      d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000))
      var expires = 'expires=' + d.toUTCString()
      console.info(cname + '=' + cvalue + '; ' + expires)
      document.cookie = cname + '=' + cvalue + '; ' + expires
      console.info(document.cookie)
    },
    // 获取cookie
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
    // 清除登录cookie
    clearCookie () {
      this.setCookie('isLogin', '', -1)
      this.setCookie('userId', '', -1)
      this.setCookie('userName', '', -1)
    }
  },
  // 生命周期函数，打开页面后自动运行
  created () {
    this.getLoginState()
    if (this.isLogin) {
      this.syncUser()
    } else {
      this.portraitSrc = require('@/assets/img/blank.png')
    }
  }
}
</script>

<style scoped>
#app {
  position: relative;
  width: 100%;
  height: 70px;
  background: #ffffff;
  border-bottom: #dcdee2 1px solid;
}

.menu {
  text-decoration: none;
  color: #333;
  width: 100%;
  height: 100%;
}

.head {
  width: 100%;
  height: 100%;
  margin: 0 auto;
}

.head-title {
  position: relative;
  float: left;
  height: 100%;
  width: 200px;
  line-height: 70px;
  text-align: center;
  font-size: 32px;
  color: #2d8cf0;
  margin-left: 20px;
}

.head-title1 {
  height: 100%;
  width: 100px;
  line-height: 70px;
  text-align: center;
  font-size: 18px;
  color: black;
}

.user-bar {
  float: right;
  height: 100%;
  width: 180px;
  margin-top: 10px;
}

.head-icon1 {
  position: relative;
  float: left;
  margin-top: 14px;
  width: 60px;
  height: 100%;
}

.head-icon2 {
  position: relative;
  float: left;
  margin-top: 14px;
  width: 60px;
  height: 100%;
}

.user-portrait {
  float: right;
  right: 10px;
  top: -42px;
}

#userInfor,
#userInforModify {
  width: 100%;
  height: 100%;
}

.user-head {
  width: 100%;
  height: 220px;
}

.user-protraitLarge {
  width: 100px;
  height: 100px;
  border-radius: 100%;
  overflow: hidden;
}

.user-head button {
  position: relative;
  float: right;
  top: 68px;
}

.user-infor {
  position: relative;
  width: 100%;
  height: 120px;
}

.infor-name {
  width: 100%;
  font-size: 28px;
  color: #17233d;
}

/* 用户详细信息，粉丝、关注和主题数 */
.infor-detail {
  float: left;
  margin-top: 10px;
  width: 60px;
  color: #515a6e;
  font-size: 14px;
}

/* 用户头像 */
.infor-autograph {
  margin-top: 8px;
  float: left;
  width: 420px;
  font-size: 14px;
}

.user-detail {
  width: 100%;
  height: 300px;
}

.modify-head {
  width: 100%;
  height: 200px;
}

.upload {
  position: relative;
  float: right;
  top: 68px;
}

.modify-title {
  width: 100%;
  font-size: 16px;
  margin-top: 20px;
}

.modify-input {
  width: 150px;
  margin-top: 10px;
}
</style>
