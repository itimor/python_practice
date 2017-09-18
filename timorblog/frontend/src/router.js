'use strict';
import Vue from 'vue'
import store from './vuex/store'
import {mapState, mapActions} from 'vuex'
import VueRouter from 'vue-router'
import axios from 'axios'

Vue.use(VueRouter);

const routes = [
  {
    path: '/login',
    name: '登录',
    component: function (resolve) {
      require(['./views/login.vue'], resolve)
    },
    hidden: true  // 自定义的属性，目的是在遍历菜单时，过滤不需要的菜单项
  },
  {
    path: '/404',
    name: '404',
    component: require('./views/error/404.vue'),
    hidden: true
  },
    {
        path: '/',
        hidden: true,
        redirect: { path: '/posts' }
    },
  {
    path: '/posts',
    name: '博客',
    component: require('./views/blog/Index.vue'),
    children: [
      {name: '博客列表', path: '/posts', component: require('./views/blog/Posts.vue')},
      {name: '文章筛选', path: '/:label/:title', component: require('./views/blog/Posts.vue')},
    ]
  },
    {
    path: '/admin',
    name: '管理',
    meta: {requiresAuth: true},
    component: require('./views/admin/index.vue'),
  },
  {
        path: '*',
        hidden: true,
        redirect: { path: '/404' }
    }
];


const router = new VueRouter({
  mode: 'history', //  hash 模式  history 模式
  base: '/', // 默认值: "/",应用的基路径。例如，如果整个单页应用服务在 /app/ 下，然后 base 就应该设为 "/app/"。
  routes
});

// 设置路由拦截
// 在vue-router的全局钩子中设置拦截
// 每个路由皆会的钩子函数
// to 进入 from 离开 next 传递
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.state.isLogin) {
      //存在authorization信息，则验证下。
        _checkToken().then(function () {
          next();
        },function () {
          next({
            path: '/login'
          })
        });
    } else {
      _checkToken().then(function () {
        next();
      },function () {
        next({
          path: '/login'
        })
      });
    }
  } else {
    next(); // 确保一定要调用 next()
  }
})

/**
 * Token验证，Token验证是否有效，时间验证过期
 * */
function _checkToken() {
  return new Promise(function (resolve, reject) {
    let token = localStorage.getItem('token');
    let token_time = parseInt(localStorage.getItem('token_time'));
    var now_time = new Date().getTime();  // 毫秒数，token过期时间为 2小时
    if (token && (now_time - token_time) < 1000 * 60 * 60 * 2) {
      //token有效,能进入
      store.dispatch('setLoginState',true);
      // 设置全局请求的token， 参考 https://segmentfault.com/q/1010000008595567/a-1020000008596744
      axios.interceptors.request.use(
        config => {
        config.headers.Authorization = `token ${token}`;
      return config;
      },err => {
        return Promise.reject(err);
      });
      resolve();
    } else {
      localStorage.removeItem('token');
      localStorage.removeItem('token_time');
      store.dispatch('setLoginState',false);
      reject();
    }
  })
}

export default router
