<template>
  <div class="posts">
    <blog :blogdata="blogdata" v-on:currentPage="getBlogData"></blog>
  </div>
</template>

<script>
  import Blog from './layout/Blog.vue'
  import {getblogList} from '@/api/blog'
  import {LIMIT} from '@/config'

  export default {
    name: 'posts',

    components: {Blog},
    data() {
      return {
        args: {
          published: true,
          ordering: '-publish_time',
          slug: '',
          content__contains: '',
          category__title: '',
          tags__title__contains: ''
        },
        blogdata: {
          total: 0,
          list: '',
          limit: LIMIT,
          currentPage: 0,
          displaymain: true,
        }
      }
    },

    created() {
      this.getBlogData()
    },

    watch: {
      // 如果路由有变化，会再次执行该方法
      '$route': 'getBlogData',
    },

    methods: {
      getBlogData() {
        this.args.limit = this.blogdata.limit;
        this.args.offset = this.blogdata.currentPage - 1;
        this.blogdata.displaymain = true;
        if (this.$route.params.label === 'category') {
          this.args.category__title = this.$route.params.title;
          document.title = "文章归类"
        } else if (this.$route.params.label === 'tag') {
          this.args.tags__title__contains = this.$route.params.title;
          document.title = "文章标签"
        } else if (this.$route.params.label === 'blog') {
          this.args.slug = this.$route.params.title;
          document.title = "文章详情";
          this.blogdata.displaymain = false;
        } else if (this.$route.params.label === 'content') {
          this.args.content__contains = this.$route.params.title;
          document.title = `搜索包含"${this.$route.params.title}"的文章`;
        }
        getblogList(this.args).then(res => {
          this.blogdata.list = res.data.results;
          this.blogdata.total = res.data.count
        });
      }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
</style>
