// 图像分类功能页面
<template>
  <div id='app'>
    <div class="sort-title">
      <h1>图像分类</h1>
      <p>请上传需要进行识别的图片</p>
    </div>
    <div class="sort-img">
      <el-upload action="https://jsonplaceholder.typicode.com/posts/"
                 list-type="picture-card"
                 :on-preview="handlePictureCardPreview"
                 :on-remove="handleRemove">
        <i class="el-icon-plus"></i>
      </el-upload>
      <el-dialog :visible.sync="dialogVisible">
        <img width="100%"
             :src="dialogImageUrl"
             alt="">
      </el-dialog>
    </div>
    <div class="operation">
      <el-button @click="clean">重新选择</el-button>
      <el-button @click="start">开始识别</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'sort',
  data () {
    return {
      dialogImageUrl: '',
      dialogVisible: false
    }
  },
  components: {

  },
  methods: {
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePictureCardPreview (file) {
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    },
    // 清空重新选择图片
    clean () {

    },
    // 开始识别图像
    start () {

    }
  }
}
</script>
<style>
* {
  margin: 0;
  padding: 0;
}
.sort-title {
  width: 100%;
  height: 90px;
  text-align: center;
  margin-top: 0px;
}

.sort-title h1 {
  margin: 10px 0px;
}

.sort-title p {
  width: 100%;
  line-height: 100%;
  margin: 10px 0px;
  font-size: 16px;
}

/* 图像分类主面板 */
.sort-img {
  /* width: 1150px; */
  width: 1310px;
  min-height: 320px;
  margin: 0 auto;
  padding: 30px 10px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.operation {
  margin: 30px;
}
</style>
