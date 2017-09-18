<template>
  <div class="posts">
    <blog :blogdata="blogdata"></blog>
  </div>
</template>

<script>
  import Blog from './Blog.vue'
  import { getblogList } from '@/api/blog'

  export default {
    name: 'posts',

    components: {Blog},
    data() {
      return {
        args: {
          published: true,
          ordering: 'access_count',
          limit: 5,
        },
        blogdata: {
          total: 0,
          list: '',
          displayhot: false
        }
      }
    },

    created() {
      this.getBlogData()
    },

    methods: {
      getBlogData() {
        this.blogdata.displayhot = true;
        getblogList(this.args).then(res => {
          this.blogdata.list = res.data.results;
          this.blogdata.total = res.data.count
      })
      }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
</style>
