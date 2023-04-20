function greet(name) {
  return "Hello, " + name + "!";
}
let result = greet("John");
console.log(result);


// 声明一个匿名函数
let greetPram = function (name) {
  return "Hello, " + name + "!";
};
let result2 = greetPram('张三')
console.log(result2)

// 箭头函数，也是一种匿名函数
let sumFun = (param1, param2) => {
    return param1 + param2;
};
console.log(sumFun(1, 2));
