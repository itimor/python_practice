import * as types from './mutation-types'

// 对于vuex的用法，其实理解了流程就行
// vuex -> actions -> 提交（commit）mutations ->state -> view -> dispatch 触发 actions ->...
// actions 其实是mutations的升级版，它实现了mutations只能同步改变状态不能异步改变
// actions 就是可以异步操作mutation的提交
// 具体可以看下我的blog中的总结 http://selvinpro.com/2017/03/17/vuex-about/#more
export const mutations = {
  // 这里的data指提交时：
  // 从/api/login传回的token，其中包含name,messeage等信息
  [types.LOGIN](state, data) {
      // 将token和username储存在本地
      localStorage.setItem('token', data.token);
      state.token = data.token;
      localStorage.setItem('username', data.username);
      state.username = data.username,
      localStorage.setItem('token_time', data.token_time),
      state.token_time = data.token_time
      // vuex的本质作用是管理组件之间复杂的状态的（如购物车逻辑等等...）
      // 所以当刷新浏览器时，这些状态也会一并被清空
      // 所以还是需要有一个长期在浏览器中保存如登录/登出状态的机制
      // 因此这里采用了localStorage
      // 一定要明白vuex这类库的本质作用，它极大的增加了前端逻辑处理的可能性
  },
  [types.LOGINOUT](state) {
      localStorage.removeItem('token');
      state.token = null
      localStorage.removeItem('username');
      state.username = null;
  },

  [types.LOGIN_STATUS] (state, status) {
      state.isLogin = !!status;
  },

  [types.POST_ARGS] (state, data) {
      state.post_args = data;
      const postdata = JSON.stringify(data); //localStorage存储JSON对象时需要先把数据转换成字符串,取值时用JSON.parse解析成JSON对象
      localStorage.setItem('post_args', postdata);
  }
};

export default mutations
