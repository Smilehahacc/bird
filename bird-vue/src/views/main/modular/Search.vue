// 图片搜索下载（爬虫）功能页面
<template>
  <div class="block">
    <span class="demonstration">时 间</span>
    <el-date-picker
      v-model="timevalue"
      align="center"
      type="daterange"
      range-separator="-"
      start-placeholder="开始日期"
      end-placeholder="结束日期">
    </el-date-picker>
  </div>
</template>

<script>
export default {
  name: 'search',
  data () {
    return {
      timevalue: ''
    }
  },
  components: {

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
