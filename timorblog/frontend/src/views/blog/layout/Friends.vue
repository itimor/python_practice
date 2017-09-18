<template>
  <div class="items">
        <ul class="aside-list">
          <li class="aside-item" v-for="item in list" :key="item.id">
            <a :href="item.link" target="_blank">{{item.title}}</a>
          </li>
        </ul>
  </div>
</template>

<script>
  import { getfriendList } from '@/api/friend'

  export default {
    name: 'friends',

    props: ['args'],
    data() {
      return {
        total: 0,
        list: ''
      }
    },

    created() {
      this.getFriendList();
    },

    methods: {
      getFriendList() {
        getfriendList(this.args).then(res => {
          this.list = res.data.results;
          this.total = res.data.count
      })
      }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
</style>
