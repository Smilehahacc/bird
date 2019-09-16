// 图片搜索下载（爬虫）功能页面
<template>
  <div id='app'>
    <el-card class="box-card">
      <div class="header">
        <el-input
          placeholder="请输入爬取内容"
          suffix-icon="el-icon-search"
          v-model="inputdata">
        </el-input>
      </div>
      <el-date-picker
        v-model="timevalue"
        align="center"
        value-format="yyyy-MM-dd"
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
          <el-button @click="pushdata()">启动</el-button>
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
      currentRow: null,
      inputdata: '',
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
    // 重置函数 重置时间和来源
    setCurrent (row) {
      this.inputdata = ''
      this.timevalue = ''
      this.$refs.singleTable.setCurrentRow(row)
    },
    // 启动函数 给后台传值 暂时写成弹窗
    pushdata () {
      console.log(this.inputdata)
      console.log(this.timevalue)
      console.log(this.currentRow.source)
    },
    // 点击时期选择器后存值
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
.header {
  width: 350px;
  height: 50px;
  margin: 0 auto;
}
.hinput {
  float: left;
}
</style>
