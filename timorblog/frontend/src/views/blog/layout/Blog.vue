<template>
  <div class="items">
    <div v-if="blogdata.displayhot">
      <ul class="aside-list">
        <li class="aside-item" v-for="post in blogdata.list" :key="post.slug">
          <a :href="'/blog/'+post.slug">{{post.title}}</a>
        </li>
      </ul>
    </div>
    <el-card v-else class="el-card__body" v-for="post in blogdata.list" :key="post.slug">
      <div class="post-header">
        <el-tooltip content="归档" placement="top">
          <category class="category" :args="{'title':post.category}"></category>
        </el-tooltip>
        <div class="post-title">
          <a :href="'/blog/'+post.slug">{{post.title}}</a>
        </div>
      </div>
      <div>
        <icon name="tags"></icon>
        <tag-cloud class="post-tags" v-for="tag in post.tags" :key="tag.title" :args="{'title':tag}"></tag-cloud>
        <div class="post-header-info">
          <icon class="icon" name="calendar"></icon>
          <a>{{post.publish_time | toDate}}</a>
          <icon class="icon" name="eye"></icon>
          <a v-text="post.access_count"></a>
        </div>
      </div>
      <hr class="line"/>

      <blog-content :post="post" :displaymain="blogdata.displaymain"></blog-content>
    </el-card>

    <div class="pagination">
      <el-pagination
        v-show="blogdata.displaymain"
        small
        @current-change="handleCurrentChange"
        :current-page.sync="blogdata.currentPage"
        :page-size="blogdata.limit"
        layout="prev, pager, next, total"
        :total="blogdata.total">
      </el-pagination>
    </div>
  </div>
</template>

<script>
  import TagCloud from './Tags.vue'
  import Category from './Categorys.vue'
  import blogContent from './BlogContent.vue'

  export default {
    name: 'blogs',

    props: ['blogdata'],
    components: {TagCloud, Category, blogContent},
    data() {
      return {}
    },

    created() {
    },

    methods: {
      handleCurrentChange(){
        this.$emit("currentPage", this.blogdata.currentPage);
      }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .el-card__body {
    margin-bottom: 2%;
    padding: 2px;
  }

  .category {
    float: left;
    margin-right: 8px;
  }

  .post-title {
    color: #1781ff;
    font-size: 1.5rem;
  }

  .post-header-info {
    display: inline-block;
    font-size: 1em;
    color: #818181;
    float: right;
    padding-top: 5px;
  }

  .line {
    margin-bottom: 10px;
    height: 1px;
    border: 0;
    background-color: #D5D5D5;
    color: #D5D5D5;
  }

  .post-tags {
    display: inline-block;
    margin-right: 5px;
  }

  .pagination {
    text-align: center;
  }

  .icon {
    color: #23c9ff;
  }
</style>
