// 算法效率评估页面
<template>
<el-card class="box-card">
  <div id="app">
    <h1>算法评估</h1>
    <br>
    <el-upload
      class="avatar-uploader"
      action="https://jsonplaceholder.typicode.com/posts/"
      :show-file-list="false"
      :on-success="handleAvatarSuccess"
      :before-upload="beforeAvatarUpload"
    >
      <img v-if="imageUrl" :src="imageUrl" class="avatar" />
      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
    </el-upload>
    <el-button @click="clean">开始识别</el-button>
    <div class='biaoge'>
    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="date" label='算法' width="180"></el-table-column>
      <el-table-column prop="name" label='分析结果' width="180"></el-table-column>
    </el-table>
    </div>
  </div>
</el-card>
</template>

<script>
export default {
  name: 'algorithm',
  data () {
    return {
      imageUrl: '',
      tableData: [
        {
          date: '算法1',
          name: '80%是鸟'
        },
        {
          date: '算法2',
          name: '99%是鸟'
        }
      ]
    }
  },
  methods: {
    handleAvatarSuccess (res, file) {
      this.imageUrl = URL.createObjectURL(file.raw)
    },
    beforeAvatarUpload (file) {
      const isJPG = file.type === 'image/jpeg'
      const isLt2M = file.size / 1024 / 1024 < 2

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!')
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!')
      }
      return isJPG && isLt2M
    }
  }
}
</script>
<style>
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
.biaoge {
  position:absolute;
  left:650px;
  top:520px;
}
</style>
