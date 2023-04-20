function funout(){
    function funin(name){
        return name+'我是内部的函数调用....'
    }
    return funin
}

result = funout()('我可以传参')
console.log(result)

/*
    在函数内部修改外部的全局参数
    在JS逆向中可以进行函数的重写
 */
var globalParam;
function funout2(){
    function funin(){
        return '我是内部的函数调用....'
    }
    globalParam = funin
}
funout2()
result = globalParam()
console.log(result)