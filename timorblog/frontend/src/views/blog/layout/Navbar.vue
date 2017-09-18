<template>
  <el-row>
    <el-col :span="4">
    </el-col>
    <el-col>
      <el-menu class="navbar__menu" :default-active="activeIndex" mode="horizontal">
        <router-link v-for="item in menulist" :key="item.title" :to="item.href">
        <el-menu-item class="el-menu-item" :router="true" :index="item.index">
          {{item.title}}
        </el-menu-item>
        </router-link>
        <el-menu-item class="el-menu-item" index="6">
          <el-dropdown trigger="hover" v-on:command="handleNavDropdownCommand">
            <span class="el-dropdown-link">admin <i class="el-icon-caret-bottom el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown" class="navbar__dropdown-menu">
              <el-dropdown-item>个人信息</el-dropdown-item>
              <el-dropdown-item>修改密码</el-dropdown-item>
              <el-dropdown-item command="logout" divided>退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </el-menu-item>
      </el-menu>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: 'navbar',
    data() {
      return {
        activeIndex: '1',
        menulist: [
          {index: "1", title: "首页", href: '/posts'},
          {index: "2", title: "相册", href: '/photography'},
          {index: "3", title: "有色", href: '/meinv'},
          {index: "4", title: "关于", href: '/about'}
        ]
      }
    },
    methods: {
      handleNavDropdownCommand(command) {
        if (command == 'logout') {
          this.$confirm('确认退出吗?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(function () {
            this.$message('你的退出逻辑');
          }.bind(this));
        }
      },
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .navbar__menu {
    float: right;
    background-color: #fff;
  }

  .el-menu-item:hover {
    background-color: #fff;
    border-bottom: 5px solid #4ac8ff;
  }
</style>
