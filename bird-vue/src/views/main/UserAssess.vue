<template>
  <div id='app'>
     <h1 style="margin: 20px auto">为我们的系统打个分吧～</h1>
    <el-rate v-model="value"
             show-text
             style="height: 100px">
    </el-rate>
  </div>
</template>

<script>
export default {
  name: 'userAssess',
  data () {
    return {
      value: null
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
