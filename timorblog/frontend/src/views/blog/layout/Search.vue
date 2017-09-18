<template>
    <el-input
      placeholder="搜索文章..."
      icon="search"
      v-model="search"
      :on-icon-click="handsearchClick"
      @keyup.enter.native="handsearchClick">
    </el-input>
</template>

<script>
  export default {
    name: 'search',

    props: ['args'],
    data() {
      return {
        search: ''
      }
    },

    created() {
    },

    methods: {
      handsearchClick(se) {
        this.$router.push(`/content/${this.search}`)
      }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
</style>
