// 图像分类功能页面
<template>
  <div id='app'>
    <div class="sort-title">
      <h1>图像分类</h1>
      <p>请上传需要进行识别的图片</p>
    </div>
    <!-- 上传图像控件 -->
    <transition enter-active-class="animated fadeInRight">
      <div class="sort-img"
           v-if="!isStart"
           v-loading="loading">
        <el-upload action="https://jsonplaceholder.typicode.com/posts/"
                   ref="uploadedImg"
                   list-type="picture-card"
                   :on-preview="handlePictureCardPreview"
                   :on-remove="handleRemove"
                   :on-error="uploadError"
                   :on-exceed="uploadExceed"
                   :limit="maxImg"
                   :on-success="uploadSuccess">
          <i class="el-icon-plus"></i>
        </el-upload>
        <el-dialog :visible.sync="dialogVisible">
          <img width="100%"
               :src="dialogImageUrl"
               alt="">
        </el-dialog>
      </div>
    </transition>

    <!-- 展示识别结果 -->
    <transition enter-active-class="animated fadeInRight">
      <div class="sort-show"
           v-if="isStart"
           v-loading="loading">
        <div style="width: 190px; height: 180px;float: left;margin: 0 0 12px 20px;"
             v-for="fit in uploadList"
             :key="fit">
          <el-image style="width: 180px;height: 150px; margin:5px 10px;"
                    :src="require('@/assets/test/'+fit.url)"></el-image><br>
          <span style="font-size: 18px">{{ fit.sort }}</span>
        </div>

      </div>
    </transition>

    <div class="operation"
         v-if="!isStart">
      <el-button @click="clear">重新选择</el-button>
      <el-button @click="start">开始识别</el-button>
    </div>
    <div class="operation"
         v-if="isStart">
      <el-button @click="reStart">重新选择</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'sort',
  data () {
    return {
      maxImg: 10, // 最大图片上传数量
      dialogImageUrl: '',
      dialogVisible: false,
      isStart: false,
      uploadList: [],
      fits: ['fill', 'contain', 'cover', 'none', 'scale-down'],
      loading: false
    }
  },
  components: {

  },
  methods: {
    // 点击已上传图片
    handlePictureCardPreview (file) {
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    },
    // 移除图片
    handleRemove (file, fileList) {
      this.$message.success('删除成功！')
    },
    // 文件上传失败
    uploadError () {
      this.$message.error('上传失败（只能上传jpg/png文件）')
    },
    // 上传数量超出限制
    uploadExceed () {
      this.$message.warning('最多只能上传' + this.maxImg + '张图片哦～')
    },
    // 清空重新选择图片
    clear () {
      this.$message.success('列表清空成功，请重新选择需要上传的图片')
      this.uploadList = []
      this.$refs.uploadedImg.clearFiles()
    },
    // 重新选择，情况刚才已上传的图像列表
    reStart () {
      this.isStart = false
      this.$message.success('重新选择想要识别的图像吧！')
      this.uploadList = []
      this.$refs.uploadedImg.clearFiles()
    },
    uploadSuccess (response, file, fileList) {
      this.uploadList.push({
        url: file.name,
        sort: '暂无分类'
      })
    },
    // 开始识别图像
    start () {
      if (this.uploadList.length === 0) {
        this.$Message.warning('至少上传一张图片哦～')
        return
      }
      this.$Message.success('正在识别...')
      this.loading = true
      this.$axios.get('/imgSort', {
        params: {
          uploadList: JSON.stringify(this.uploadList)
        }
      }).then(response => {
        if (response.data !== 'ERROR') {
          this.uploadList = response.data
          this.isStart = true
        } else {
          this.$Message.error('识别失败！')
        }
        this.loading = false
      }).catch(error => {
        console.log(error)
        this.$Message.error('请求失败！' + error.status + ',' + error.statusText)
        this.loading = false
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
.sort-title {
  width: 100%;
  height: 90px;
  text-align: center;
  margin-top: 0px;
}

.sort-title p {
  width: 100%;
  line-height: 100%;
  margin: 10px 0px;
  font-size: 16px;
}

/* 图像分类主面板 */
.sort-img,
.sort-show {
  /* width: 1150px; */
  width: 1310px;
  min-height: 420px;
  margin: 0 auto;
  padding: 30px 10px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.operation {
  margin-top: 30px;
}

</style>
