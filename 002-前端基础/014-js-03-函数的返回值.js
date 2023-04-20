// 箭头函数，也是一种匿名函数
let sumFun2 = (param1, param2) => {
    return param1 + param2, param1 - param2;  // 会返回最后一个表达式的值 , ","表示语句还没有执行完, 会继续执行后面的表达式
};
console.log(sumFun2(1, 2));

// 箭头函数，也是一种匿名函数
let sumFun3 = (param1, param2) => {
    return param1 + param2; param1 - param2;  //会返回前面一个表达式的值 , 因为已经return了 ,不会再执行后面的表达式
};
console.log(sumFun3(1, 2));
