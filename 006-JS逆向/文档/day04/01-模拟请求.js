//发送请求

const axios = require('axios')

//设置请求拦截器
axios.interceptors.request.use(function (config) {
    console.log('请求拦截器 成功')
    config.headers['sign'] = 'exs4CQYVFQ1Udg4WPjl7XgA1Mlk4WlVHUFkISwhXUgQaI0dKS0MHCANUVVMMBiFBUA%3D%3D'
    config.headers.token = '123123123'
    return config;
}, function (error) {
    console.log('请求拦截器 失败')
    return Promise.reject(error);
});

//设置响应拦截器
axios.interceptors.response.use(function (response) {
    console.log('响应拦截器 成功')
    console.log('调解密函数进行解密数据')
    //return response;
    // return response; //修改响应数据
    return {'name':'夏洛到此一游！'}; //修改响应数据
}, function (error) {
    console.log('响应拦截器 失败')
    return Promise.reject(error);
});



axios.get('http://httpbin.org/get').then(res=>console.log(res))


