<template>
  <div id='main'>
    <div id='inputMain'>
      <div class='login-main'
           v-bind:style='{display: displayLogin}'>
        <!-- <p class='title'>{{ appTitle }}</p> -->
        <img :src="require('@/assets/img/logo_title.png')"
             class="title-logo">
        <p class='tilte-detail'>{{ loginTitle }}</p>
        <div id='inputDetail'>
          <input type="text"
                 v-model="username"
                 class='input-style'
                 placeholder="请输入手机号或用户名" /><br />
          <input type="password"
                 v-model="password"
                 class='input-style'
                 placeholder="密码" /><br />
          <Button class='button-left'
                  type="text">{{ smsLogin }}</Button>
          <Button class='button-right'
                  type="text">{{ forget }}</Button>
          <Button type="primary"
                  @click='login'
                  class='button-log'>登录</Button>
        </div>
      </div>

      <div class='register-main'
           v-bind:style='{display: displayRegister}'>
        <img :src="require('@/assets/img/logo_title.png')"
             class="title-logo">
        <p class='tilte-detail'>{{ registerTitle }}</p>
        <div id='inputDetail'>
          <input type="text"
                 v-model="phone"
                 class='input-style'
                 placeholder="手机号" /><br />
          <input type="text"
                 v-model="code"
                 class='input-style'
                 placeholder="请输入6位短信验证码" /><br />
          <Button type="text"
                  :disabled='disabled'
                  @click="sendSms"
                  class="button-sendSms">{{ btntxt }}</Button>
          <Button class='button-right'
                  type="text">{{ voice }}</Button>
          <Button type="primary"
                  @click='register'
                  class='button-log'>注册</Button>
        </div>
      </div>

      <!-- 底部选择登陆或者注册 -->
      <div id='bottomMain'>
        <p style='font-size:14px;text-align:center;width:160px;margin: 0 auto;line-height:60px;'>{{ bottomTips }}
          <Button class='button-bottom-choice'
                  type="text"
                  style='font-size:14px;outline: none;text-align:center;margin: 0 auto; color:#2b85e4;'
                  @click='choice'>{{ bottomTitle }}</Button>
        </p>
      </div>
    </div>

    <!-- 页面最底部文字 -->
    <div id='pageBottom'>
      <p>Copyright©2019 Lynn</p>
    </div>
  </div>
</template>
<script>
// 固定写法，参数的赋值
export default {
  name: 'login',
  data () {
    return {
      userInfor: [],
      appTitle: '知乎',
      loginTitle: '登录在线识图',
      registerTitle: '注册在线识图',
      smsLogin: '手机号验证登录',
      forget: '忘记密码？',
      voice: '接收语音验证码',
      bottomTips: '没有账号？',
      bottomTitle: '注册',
      btntxt: '获取短信验证码',
      time: 0,
      choiceFlag: true,
      displayLogin: '',
      displayRegister: 'none',
      disabled: false,
      username: '',
      password: '',
      phone: '',
      code: '',
      isLogin: '',
      userId: ''
    }
  },
  // 一些页面交互相关方法
  methods: {
    // 登录请求发送
    login () {
      if (this.username === '') {
        this.$Message.warning('请输入用户名或手机号！')
      } else if (this.password === '') {
        this.$Message.warning('请输入密码！')
      } else {
        // 将json对象转化为字符串直接拼接在url后面进行请求
        let postData = {
          username: this.username,
          password: this.password
        }
        this.$axios.get('/login', {
          params: {
            ...postData
          }
        }).then(response => {
          console.log(1)
          console.log(response)
          // 成功则弹出提示，跳转页面
          if (response.data === 'SUCCESS') {
            this.$Message.success('登录成功！')
            this.setCookie('userName', this.username, 7)
            this.getUserId()
            // this.$router.push('/forumCenter')
          } else {
            this.$Message.error('用户名或密码错误！')
          }
        }).catch(error => {
          console.log(error)
          this.$Message.error('请求失败！' + error.status + ',' + error.statusText)
        })
      }
    },
    getUserId () {
      this.$axios
        .get('/findUser', {
          username: this.username
        })
        .then(data => {
          console.log('获取用户基本信息------------------')
          this.userInfor = data.data
          this.userId = this.userInfor.user_id
          this.setCookie('userId', this.userId, 7)
          this.setCookie('userInfor', this.userInfor, 7)
        })

      setTimeout(() => {
        // alert("yonghuid2")
        // 更新信息，跳转页面
        this.$store.state.isLogin = true
        this.$store.state.userId = this.userId
        this.$store.state.userName = this.username
        this.setCookie('isLogin', 'true', 7)
        this.$router.push('/home')
      }, 500)
    },
    // 发送验证码
    sendSms () {
      var reg = 11 && /^((13|14|15|17|18)[0-9]{1}\d{8})$/
      if (this.phone === '') {
        this.$Message.error('请输入手机号码！')
      } else if (!reg.test(this.phone)) {
        this.$Message.warning('手机格式不正确！')
      } else {
        this.$axios.get('/sendSms', {
          params: {
            phone: this.phone
          }
        }).then(response => {
          var result = response.data
          // 通过手机号验证则开始倒计时，若手机号已注册则弹出提示
          if (result !== 'ERROR') {
            this.$Message.success('验证码已发送，请注意查收！')
            this.time = 60
            this.disabled = true
            this.setCookieMin(this.phone, result, 5)
            this.timer()
          } else {
            this.$Message.warning('手机号已注册，可直接登录！')
          }
        })
      }
    },
    timer () {
      if (this.time > 0) {
        this.time--
        this.btntxt = this.time + 's后重新获取'
        setTimeout(this.timer, 1000)
      } else {
        this.time = 0
        this.btntxt = '重新获取短信验证码'
        this.disabled = false
      }
    },
    // 注册请求处理，验证码发送
    register () {
      var reg = 11 && /^((13|14|15|17|18)[0-9]{1}\d{8})$/
      if (this.phone === '') {
        this.$Message.error('请输入手机号码！')
      } else if (!reg.test(this.phone)) {
        this.$Message.warning('手机格式不正确！')
      } else if (this.code === '') {
        this.$Message.error('请输入验证码')
      } else if (this.code === this.getCookie(this.phone)) {
        this.$axios.get('/register', {
          params: {
            phone: this.phone,
            code: this.code
          }
        }).then(response => {
          if (response.data === 'SUCCESS') {
            this.$Message.success('注册成功！')
          } else {
            this.$Message.warning('注册失败，手机号已被注册！')
          }
        }).catch(error => {
          console.log(error)
          this.$Message.error('请求失败！' + error.status + ',' + error.statusText)
        })
      } else {
        this.$Message.warning('注册失败，请检查输入的验证码')
      }
    },
    // 选择登陆或者注册，页面切换
    choice () {
      if (this.choiceFlag) { // 跳转到注册
        this.displayLogin = 'none'
        this.displayRegister = ''
        this.bottomTips = '已有帐号？'
        this.bottomTitle = '登录'
      } else { // 跳转打炮登录
        this.displayLogin = ''
        this.displayRegister = 'none'
        this.bottomTips = '没有帐号？'
        this.bottomTitle = '注册'
      }
      this.choiceFlag = !this.choiceFlag
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
    // 设置cookie
    setCookieMin (cname, cvalue, min) {
      var d = new Date()
      d.setTime(d.getTime() + (min * 60 * 1000))
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
    }
  },
  // 生命周期函数，打开页面后自动运行
  created () {

  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

#main {
  position: absolute;
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  background-image: url("../../assets/img/back.png");
  background-size: 100% 100%;
}

#inputMain {
  position: relative;
  height: 500px;
  width: 435px;
  background-color: rgb(255, 255, 255);
  align-content: center;
  margin: 0 auto;
  margin-top: 70px;
  border: 1px #dcdee2 solid;
}

#inputDetail {
  position: relative;
  width: 350px;
  height: 260px;
  margin: 0 auto;
}

.login-main {
  position: relative;
  height: 440px;
}

.register-main {
  position: relative;
  height: 440px;
  /* display: none; */
}

.title {
  padding-top: 20px;
  color: #2d8cf0;
  font-weight: bold;
  font-size: 56px;
}

.title-logo {
  height: 106px;
  width: auto;
  padding: 30px 0 10px 0;
  color: #2d8cf0;
  font-weight: bold;
  font-size: 56px;
}

.tilte-detail {
  font-size: 26px;
  font-weight: bold;
  color: #2d8cf0;
  letter-spacing: -4px;
}

.input-style {
  margin-top: 20px;
  font-size: 16px;
  height: 50px;
  width: 100%;
  border-bottom: #dcdee2 1px solid;
  border-left-width: 0px;
  border-right-width: 0px;
  border-top-width: 0px;
  /* border:0; */
  outline: none;
}

.button-sendSms {
  position: absolute;
  float: left;
  padding: 0;
  z-index: 99;
  top: 104px;
  padding: 0;
  right: 0px;
  color: #2b85e4;
}

.button-left {
  margin-top: 10px;
  padding: 0;
  float: left;
  text-align: left;
  color: #808695;
}

.button-right {
  margin-top: 10px;
  padding: 0;
  float: right;
  text-align: right;
  color: #808695;
}

.button-log {
  width: 100%;
  height: 40px;
  margin-top: 40px;
  font-size: 16px;
  color: white;
}

#bottomMain {
  height: 60px;
  font-size: 60px;
  background-color: #f8f8f9;
}

#pageBottom {
  position: relative;
  width: 100%;
  height: 60px;
  margin-top: 40px;
  text-align: center;
  color: #f8f8f9;
  font-size: 14px;
}
</style>
