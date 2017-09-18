<template>
  <div class="app-wrapper">
    <div class="sidebar-wrapper">
      <navbar></navbar>
    </div>
    <div class="main-container">
      <el-row :gutter="20">
        <el-col :sm={span:20,offset:2} :md={span:16,offset:4} :lg={span:16,offset:4}>
          <el-row :gutter="20">
            <el-col :span="16">
              <app-main></app-main>
            </el-col>
            <el-col :span="8">
              <sidebar></sidebar>
            </el-col>
          </el-row>
          <hr class="line"/>
        </el-col>
      </el-row>
    </div>
    <blog-footer></blog-footer>
  </div>
</template>

<script>
  import { Navbar, Sidebar, AppMain, blogFooter } from '@/views/blog/layout';

  export default {
    name: 'layout',
    components: {
      Navbar,
      Sidebar,
      AppMain,
      blogFooter
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .main-container {
    margin-top: 10px;
  }

  .line {
    margin-bottom: 5px;
    height: 1px;
    border: 0;
    background-color: #D5D5D5;
    color: #D5D5D5;
  }
</style>
