// 通过 arguments 获取函数的参数
let argumentFun = function () {
  return "Hello, " + arguments[0] + "!";
};
console.log(argumentFun('张三'))


// 通过形参接收参数
let sumFun = function (num1 , num2) {
  return num1 + num2
};
console.log(sumFun(1,10))
