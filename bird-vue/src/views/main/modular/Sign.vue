// 图片标记功能页面
<template>
  <div id="app">
    <div class="sign">
    <div class="Btton-title">
      <el-button type="primary" class="titleButton" plain  @click='refresh'>刷新标注</el-button>
      <el-button type="primary" class="titleButton" plain >点击提交</el-button>
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
      images: [
        {
          url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          sort: '鸟类'
        },
        {
          url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          sort: '鸟类'
        },
        {
          url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          sort: '鸟类'
        },
        {
          url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          sort: '鸟类'
        },
        {
          url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          sort: '鸟类'
        },
        {
          url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          sort: '鸟类'
        },
        {
          url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          sort: '鸟类'
        },
        {
          url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          sort: ''
        },
        {
          url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          sort: ''
        },
        {
          url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          sort: ''
        }
      ],
      options: [
        {
          value: '选项1',
          label: '鸟类'
        },
        {
          value: '选项2',
          label: '其他种类'
        }
      ]
    }
  },
  components: {},
  methods: {
    refresh () {
      this.images.forEach(element => {
        element.sort = ''
      })
    }
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
