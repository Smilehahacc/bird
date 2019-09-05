// 图片搜索下载（爬虫）功能页面
<template>
  <div id='app'>
    <el-card class="box-card">
      <span class="demonstration">时 间 ：</span>
      <el-date-picker
        v-model="timevalue"
        align="center"
        type="daterange"
        range-separator="——"
        start-placeholder="开始日期"
        end-placeholder="结束日期">
      </el-date-picker>
      <div class="datasource">
        <el-table
        ref="singleTable"
        :data="tableData"
        highlight-current-row
        @current-change="handleCurrentChange"
        style="width: 100%">
          <el-table-column
            type="index"
            width="50">
          </el-table-column>
          <el-table-column
            property="source"
            label="来源">
          </el-table-column>
        </el-table>
        <div style="margin-top: 20px">
          <el-button @click="setCurrent(tableData[1])">启动</el-button>
          <el-button @click="setCurrent()">重置</el-button>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'search',
  data () {
    return {
      timevalue: '',
      tableData: [{
        source: '百度'
      },
      {
        source: '搜狗'
      },
      {
        source: '谷歌'
      },
      {
        source: '360'
      }
      ]
    }
  },
  components: {

  },
  methods: {
    setCurrent (row) {
      this.$refs.singleTable.setCurrentRow(row)
    },
    handleCurrentChange (val) {
      this.currentRow = val
    }
  }
}
</script>
<style>
* {
  margin: 0;
  padding: 0;
}
</style>
