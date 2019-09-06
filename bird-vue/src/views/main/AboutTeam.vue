<template>
  <div id='app'>
    <h1 style="margin: 20px auto">我们的团队 (//∇//)</h1>
    <div class="demo-image__lazy" style="box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);margin: 0 48px;padding: 40px">
      <el-image v-for="url in urls"
                :key="url"
                :src="url"
                :preview-src-list="urls"></el-image>
    </div>
  </div>
</template>

<script>
export default {
  name: 'aboutTeam',
  data () {
    return {
      urls: [
        require('@/assets/img/team.png'),
        require('@/assets/img/team1.png'),
        require('@/assets/img/team2.png'),
        require('@/assets/img/team3.png')
      ]
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
