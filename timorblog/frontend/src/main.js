// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './vuex/store'

// element UI
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
Vue.use(ElementUI)

// markdown
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
Vue.use(mavonEditor)

// icon
import 'vue-awesome/icons'
import Icon from 'vue-awesome/components/Icon'
Vue.component('icon', Icon);

Vue.config.productionTip = false
/**
 * 发布模式禁用console.log()
 * */
 if (process.env.NODE_ENV === 'production') {
   console.log = function () {
   }
   console.warn = function () {
   }
 }


/**
 * blog 过滤器
 */
Vue.filter('toDate', (value) => {
    if (value) {
        const d = new Date(value);
        const minutes = d.getMinutes() < 10 ? '0' + d.getMinutes() : d.getMinutes()
        const hours = d.getHours() < 10 ? '0' + d.getHours() : d.getHours()
        return d.getFullYear() + '年' + (d.getMonth() + 1) + '月' + d.getDate() + '日 '
          // + hours + ':' + minutes
    }
})

Vue.filter('cutStr', (value,len) => {
  var r = /[^\x00-\xff]/g;
if(value.replace(r, "mm").length <= len) return value;
 var m = Math.floor(len/2);
 for(var i=m; i<value.length; i++) {
 if(value.substr(0, i).replace(r, "mm").length>=len) {
  return value.substr(0, i) + ' ...'
 }
 }
return value
})


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
});
