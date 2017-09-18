<template>
  <div class="post-content">

    <el-row v-if="displaymain">
      <el-col :sm={span:8} :md={span:10} :lg={span:8}>
        <div class="thumbnail">
          <a :href="'/blog/'+post.slug">
            <!--<img v-if="post.img_upload" :src="'/upload/'+post.img_upload" alt="">-->
            <img v-if="post.img_upload" src="/static/cover.jpg" alt="">
            <img v-else src="/static/cover.jpg" alt="">
          </a>
        </div>
      </el-col>
      <el-col :sm={span:18} :md={span:14} :lg={span:16}>
        <div class="content">
          <div v-if="!displaymain">{{ post.content }}</div>
          <div v-else>{{ post.content | cutStr(200)}}</div>
        </div>
      </el-col>
    </el-row>
    <el-row v-else>
      <div class="content">
        <div v-if="!displaymain">{{ post.content }}</div>
        <div v-else>{{ post.content | cutStr(200)}}</div>
      </div>
    </el-row>
    <el-button class="readmore" size="small" :plain="true" v-show="displaymain">
      <a :href="'/blog/'+post.slug">阅读全文>></a>
    </el-button>
  </div>
</template>

<script>
  export default {
    name: 'blogContent',

    props: ['post', 'displaymain'],
    data () {
      return {}
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .readmore {
    float: right;
    margin: 5px 0;
  }
</style>
