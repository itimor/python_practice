<template>
  <div class="sidebar">

    <search></search>

    <el-collapse class="sidebar-item" v-model="active1">
      <el-collapse-item title="热门文章" name="1">
        <hot></hot>
      </el-collapse-item>
    </el-collapse>

    <el-collapse class="sidebar-item" v-model="active2">
      <el-collapse-item title="文章目录" name="1">
          <category></category>
      </el-collapse-item>
    </el-collapse>

    <el-collapse class="sidebar-item" v-model="active3">
      <el-collapse-item title="文章标签" name="1">
        <tag></tag>
      </el-collapse-item>
    </el-collapse>

    <el-collapse class="sidebar-item" v-model="active4">
      <el-collapse-item title="友情链接" name="1">
        <friend></friend>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script>
  import Category from './Categorys.vue'
  import Tag from './Tags.vue'
  import Friend from './Friends.vue'
  import Search from './Search.vue'
  import Hot from './Hot.vue'

  export default {
    name: 'sidebar',

    components: {Search, Hot, Category, Tag, Friend},
    data() {
      return {
        active1: '1',
        active2: '1',
        active3: '1',
        active4: '1',
      }
    },

    created() {
    },

    methods: {
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .sidebar-item {
    margin-top: 20px;
  }

  .el-collapse-item__header {
    background-color: red;
  }
</style>
