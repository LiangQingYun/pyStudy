
// 1.导入 express
const express = require('express');

// 2.创建 web 服务器
const app = express();
// token 值

// post方法需要添加
app.use(express.json()) // json形式
app.use(express.urlencoded({extended:false}))  // 表单形式


// 实现get请求
app.get('/api', (req, res) => {
    // 调用express提供的res.send()方法，向客户端响应一个JSON对象
    pwd = req.query.pwd // 获取前端传的参数
    pwd_res = btoa(pwd) // 编码
    res.send({'pwd':pwd_res}) // 返回是json格式
})

app.get('/user/:id/:name', (req, res) => {
//    req.paraams 是动态匹配到的URL参数，默认也是一个空对象
    console.log(req.params)
    res.send(req.params)
})

// 实现post请求
app.post('/', (req, res) => {
//    req.paraams 是动态匹配到的URL参数，默认也是一个空对象
    console.log(req.body)
    res.send('请求成功')
})


// 3.启动 web 服务器
app.listen(8080, () => {
    console.log('express server running at http://127.0.0.1:8080');
})



