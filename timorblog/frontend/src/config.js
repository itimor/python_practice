/**
 * Created by Itimor on 2017/4/21.
 */

let CONFIG;
// if (process.env.NODE_ENV === 'development') {
if (process.env.NODE_ENV === 'production') {
  CONFIG = {
    apiUrl: "",
    EMAIL: 'itimor@126.com'
  };
} else {
  CONFIG = {
    apiUrl: "http://localhost:8000",
    EMAIL: 'itimor@126.com'
  };
}


//接口API根地址
const url = CONFIG.apiUrl;
const EMAIL = CONFIG.EMAIL;

module.exports = {
  //通用状态码
  SYS_ERR: 'api请求系统错误',//api请求系统错误

  //用户、登录相关
  EMAIL: EMAIL,

  //数据表限制
  LIMIT: 10,

  //登录
  login: `${url}/api-token-auth/`,
  changePassword: `${url}/api/change_password`,

  //blog
  getbloglist: `${url}/api/blog/`,

  //tags
  gettaglist: `${url}/api/tag/`,

  //category
  getcategorylist: `${url}/api/category/`,

  //friend
  getfriendlist: `${url}/api/friend/`,
};

