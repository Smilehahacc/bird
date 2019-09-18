// 图片标记功能页面
<template>
  <div id="app">
    <div class="sign">
    <div class="Btton-title">
      <el-button type="primary" class="titleButton" plain  @click='refresh'>刷新标注</el-button>
      <el-button type="primary" class="titleButton" plain @click="pushimages">点击提交</el-button>
    </div>
    <div class="line"> </div>
      <div class="block" v-for="fit in images" :key="fit">
        <div class="imagesContent">
          <el-image style="width: 200px; height: 150px; margin:20px;" :src=" fit.url"></el-image>
          <el-select v-model="fit.sort" placeholder="请选择">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          ></el-option>
        </el-select>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'sign',
  data () {
    return {
      ceshi: 'admin',
      images: [],
      options: [
        // 标注图片 0是鸟类 1是其他种类
        {
          value: '1',
          label: '鸟类'
        },
        {
          value: '0',
          label: '其他种类'
        }
      ]
    }
  },
  components: {},
  methods: {
    // 清空所有标注函数
    refresh () {
      this.images.forEach(element => {
        element.sort = ''
      })
    },
    // 获取标注图片函数
    pullimages () {
      let postData = {
        ceshi: this.ceshi
      }
      this.$axios.get('/getsign', {
        params: {
          ...postData
        }
      }).then(response => {
        console.log(response)
        response.data.images.forEach(element => {
          element.sort = ''
        },
        this.images = response.data.images
        )
      }).catch(error => {
        console.log(error)
        this.$Message.error('请求失败！' + error.status + ',' + error.statusText)
      })
    },
    // 提交标注函数
    pushimages () {
      let postData = {
        // images: this.images
        images: JSON.stringify(this.images)
        // ceshi: this.ceshi
      }
      console.log(postData)
      this.$axios.get('/pushsign', {
        params: {
          ...postData
        }
      }).then(response => {
        console.log(response)
      }).catch(error => {
        console.log(error)
        this.$Message.error('请求失败！' + error.status + ',' + error.statusText)
      })
    }
  },
  // 生命周期函数，打开页面后自动运行
  created () {
    this.pullimages()
  }
}
</script>
<style>
* {
  margin: 0;
  padding: 0;
}
.sign {
  width: 100%;
  height: 100%;
  min-height: 700px;
  float: left;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
}
.imagesContent{
  width: 20%;
  height: 20%;
  float: left;
}
.Btton-title{
  width: 100%;
  height: 70px;
}
.titleButton{
  float: right;
  width: 180px;
  height: 40px;
  margin-right: 3%;
  margin-top: 1%;
}
.line{
  width: calc(100%-100px);
  margin: 20px 50px 0px 50px;
  height: 2px;
  background-color:rgba(0, 0, 0, .12);
}
</style>
