// 算法效率评估页面
<template>
  <div id="app">
    <div class="assess-title">
      <h1>算法评估</h1>
      <p>调节参数，以获得不同评估结果</p>
    </div>
    <!-- 上传图像控件 -->
    <transition enter-active-class="animated fadeInRight">
      <div class="algorithm-assess">
        <div class="assess-area"
             v-loading="loading1">
          <p>KNN算法</p>
          <el-select v-model="choiceKnn"
                     placeholder="选择评估参数"
                     style="margin: 10px auto;width: 140px">
            <el-option v-for="item in options"
                       :key="item.value"
                       :label="item.label"
                       :value="item.value">
            </el-option>
          </el-select>
          <div class="block"
               v-if="choiceKnn==='1'?false:true">
            <p>k值(越小准确率越高，但运行时间越长)</p>
            <el-slider v-model="kValue"
                       :min=5
                       :max=15
                       style="width: 180px;margin: 10px auto"></el-slider>
          </div>
          <div class="operation"
               style="margin: 20px 0 20px 0">
            <el-button @click="knnStart">{{ isKnnStart?'重新评估':'开始评估'}}</el-button>
          </div>
          <p>准确率：{{ knnResult }}</p>
        </div>
        <div class="assess-area"
             v-loading="loading2">
          <p>BP算法</p>
          <el-select v-model="choiceBp"
                     placeholder="选择评估参数"
                     style="margin: 10px auto;width: 140px">
            <el-option v-for="item in options"
                       :key="item.value"
                       :label="item.label"
                       :value="item.value">
            </el-option>
          </el-select>
          <div class="block"
               v-if="choiceBp==='1'?false:true">
            <p>学习率值（推荐值0.1-0.5）</p>
            <el-slider v-model="learningRate"
                       :min=1
                       :max=5
                       style="width: 180px;margin: 10px auto"
                       :format-tooltip="formatTooltip"></el-slider>
          </div>
          <div class="block"
               v-if="choiceBp==='1'?false:true">
            <p>迭代次数（越多时间越长）</p>
            <el-slider v-model="epochs"
                       :min=20
                       :max=100
                       style="width: 180px;margin: 10px auto"></el-slider>
          </div>
          <div class="operation"
               style="margin: 20px 0 20px 0">
            <el-button @click="bpStart">{{ isBpStart?'重新评估':'开始评估'}}</el-button>
          </div>
          <p>准确率：{{ bpResult }}</p>
        </div>
        <div class="assess-area"
             v-loading="loading3">
          <p>SVM算法</p>
          <el-select v-model="value"
                     disabled
                     placeholder="默认参数"
                     style="margin: 10px auto;width: 140px">
            <el-option v-for="item in options"
                       :key="item.value"
                       :label="item.label"
                       :value="item.value">
            </el-option>
          </el-select>
          <div class="operation"
               style="margin: 20px 0 20px 0">
            <el-button @click="svmStart">{{ isKnnStart?'重新评估':'开始评估'}}</el-button>
          </div>
          <p>准确率：{{ svmResult }}</p>
        </div>
      </div>
    </transition>
  </div>

</template>

<script>
export default {
  name: 'algorithm',
  data () {
    return {
      isKnnStart: false,
      isBpStart: false,
      isSvmStart: false,
      choiceKnn: '',
      choiceBp: '',
      kValue: '',
      learningRate: '',
      epochs: '',
      knnResult: '暂无',
      bpResult: '暂无',
      svmResult: '暂无',
      loading1: false,
      loading2: false,
      loading3: false,
      options: [{
        value: '1',
        label: '默认参数'
      }, {
        value: '2',
        label: '自定义参数'
      }]
    }
  },
  methods: {
    // 开始knn算法评估
    knnStart () {
      if (this.choiceKnn === '') {
        this.$Message.warning('还未选择KNN算法评估模式哦～')
        return
      } else if (this.choiceKnn === '1') {
        // 设置参数的默认值
        this.kValue = 10
      }
      this.$Message.success('正在进行KNN算法准确率评估...')
      this.loading1 = true
      this.$axios.get('/getKnn', {
        params: {
          kValue: this.kValue
        }
      }).then(response => {
        if (response.data !== 'ERROR') {
          this.knnResult = response.data
          this.$Message.success('KNN算法准确率评估完成！')
        } else {
          this.$Message.error('KNN算法准确率评估失败！')
        }
        this.loading1 = false
      }).catch(error => {
        console.log(error)
        this.$Message.error('请求失败！' + error.status + ',' + error.statusText)
        this.loading1 = false
      })
    },
    // 开始bp算法评估
    bpStart () {
      if (this.choiceBp === '') {
        this.$Message.warning('还未选择BP算法的评估模式哦～')
        return
      } else if (this.choiceBp === '1') {
        // 设置参数的默认值
        this.learningRate = 0.1
        this.epochs = 50
      }
      this.$Message.success('正在进行BP算法准确率评估...')
      this.loading2 = true
      var lRate = this.learningRate
      this.$axios.get('/getBp', {
        params: {
          learningRate: parseInt(this.learningRate) / 10 + '',
          epochs: this.epochs
        }
      }).then(response => {
        if (response.data !== 'ERROR') {
          this.bpResult = response.data
          this.learningRate = lRate
          this.$Message.success('BP算法准确率评估完成！')
        } else {
          this.$Message.error('BP算法准确率评估失败！')
        }
        this.loading2 = false
      }).catch(error => {
        console.log(error)
        this.$Message.error('请求失败！' + error.status + ',' + error.statusText)
        this.loading2 = false
      })
    },
    // 开始svm算法评估
    svmStart () {
      this.$Message.success('正在进行SVM算法准确率评估...')
      this.loading3 = true
      this.$axios.get('/getSvm', {
      }).then(response => {
        if (response.data !== 'ERROR') {
          this.svmResult = response.data
          this.$Message.success('SVM算法准确率评估完成！')
        } else {
          this.$Message.error('SVM算法准确率评估失败！')
        }
        this.loading3 = false
      }).catch(error => {
        console.log(error)
        this.$Message.error('请求失败！' + error.status + ',' + error.statusText)
        this.loading3 = false
      })
    },
    formatTooltip (val) {
      return val / 10
    }
  }

}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

.assess-title {
  width: 100%;
  height: 90px;
  text-align: center;
  margin-top: 0px;
}

.assess-title p,
.assess-area p {
  width: 100%;
  line-height: 100%;
  margin: 10px 0px;
  font-size: 16px;
}

.algorithm-assess {
  /* width: 1150px; */
  width: 1310px;
  height: 420px;
  margin: 0 auto;
  padding: 30px 10px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.assess-area {
  float: left;
  width: 430px;
  height: 360px;
}
</style>
