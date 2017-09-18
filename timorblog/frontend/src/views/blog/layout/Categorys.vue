<template>
  <div class="items">
    <div v-if="displaytitle">
      <a class="category" :href="'/category/'+category.title">
        <el-tag :type="selecttype()">{{category.title}}</el-tag>
      </a>
    </div>
    <div v-else>
        <ul class="aside-list">
          <li class="aside-item" v-for="item in list" :key="item.title">
          <a :href="'/category/'+item.title">{{item.title}}</a>
          </li>
        </ul>
      </div>
  </div>
</template>

<script>
  import { getcategoryList } from '@/api/category'
  export default {
    name: 'categorys',

    props: ['args'],
    data() {
      return {
        total: 0,
        list: '',
        category: '',
        displaytitle: false,
        tagtype: ['primary','gray','success','warning','danger']
      }
    },

    created() {
      this.getCategoryList();
    },

    methods: {
      selecttype() {
        return this.tagtype[Math.floor(Math.random()*this.tagtype.length)]
      },

      getCategoryList() {
        getcategoryList(this.args).then(res => {
          if (this.args) {
            this.displaytitle = true;
            this.category = res.data.results[0];
        } else {
          this.list = res.data.results;
          this.total = res.data.count
        }
      })
      }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
</style>
