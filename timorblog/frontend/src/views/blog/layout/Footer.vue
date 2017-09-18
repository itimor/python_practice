<template>
  <div class="layout-copy">
      {{ date  }} &copy; <a href="/">撸大湿</a>; Prower by <a href="https://www.djangoproject.com/">Django</a>&<a href="https://vuejs.org">vuejs</a>

        </div>
        </template>

        <script>
          export default {
              name: 'footerBlog',

              data() {
                    return {
                            date: ''
                          }
                  },

              created() {
                    this.getDate()
                  },

              methods: {
                             getDate() {
                                     this.date = (new Date()).getFullYear()
                                   }
                           }
            }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .layout-copy {
      text-align: center;
      padding: 10px 0 20px;
      color: #9ea7b4;
    font-size: 0.6em;
    }
</style>
