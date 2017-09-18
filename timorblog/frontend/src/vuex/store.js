import Vue from 'vue'
import Vuex from 'vuex'
import mutations from './mutations'
import actions from "./actions"

Vue.use(Vuex);

const state = {
    token: null,
    username: '',
    group: '',
    token_time: '',
    isLogin: false, //是否登录
    post_args: ''
};

// 整合初始状态和变更函数，我们就得到了我们所需的 store
// 至此，这个 store 就可以连接到我们的应用中
export default new Vuex.Store({
    state,
    mutations,
    actions
})
