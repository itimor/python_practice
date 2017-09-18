<template>
  <div class="items">
    <a v-if="displaytitle" :href="'/tag/'+tag.title">
        <el-tag :color="color()">{{tag.title}}</el-tag>
    </a>
    <div>
    <a class="item" v-for="item in list" :key="item.title" :href="'/tag/'+item.title">
      <el-tag :color="color()">{{item.title}}</el-tag>
    </a>
      </div>
  </div>
</template>

<script>
  import { gettagList } from '@/api/tags';
  export default {
    name: 'tagcloud',

    props: ['args'],
    data() {
      return {
        total: 0,
        list: '',
        tag: '',
        displaytitle: false
      }
    },

    created() {
      this.getTagList();
    },

    methods: {
      color() {
        return '#' + Math.floor(Math.random() * 1000000);
      },

      getTagList() {
        gettagList(this.args).then(res => {
          if (this.args) {
            this.displaytitle = true;
            this.tag = res.data.results[0];
        } else
        {
          this.list = res.data.results;
          this.total = res.data.count
        }
      })
      }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .items {
    padding: 5px 0;
  }

  .item {
    margin: 3px;
  }
</style>
