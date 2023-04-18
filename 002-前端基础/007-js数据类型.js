/*
原始类型包括：
    number（数字类型）：整数或浮点数。
    string（字符串类型）：表示一组字符，使用单引号、双引号或反引号（ES6）来表示字符串。
    boolean（布尔类型）：表示真或假，只有两个值true和false。
    null（空类型）：表示一个空值。
    undefined（未定义类型）：表示一个未定义的值。

引用类型包括：
    Object（对象类型）：一种复合值，包括属性和方法。
    Array（数组类型）：一种特殊的对象，包括一组有序的、可访问的、可迭代的值。
    Function（函数类型）：一种具有可调用功能的对象，是 JavaScript 语言的核心。
    Date（日期类型）：一种特殊的对象，用于处理日期和时间。
    RegExp（正则表达式类型）：一种特殊的对象，用于匹配字符串。
 */

// 定义数字类型
let num = 10;
console.log(typeof num); // 输出：number

// 定义字符串类型
let str = "Hello, world!";
console.log(typeof str); // 输出：string

// 定义布尔类型
let bool = true;
console.log(typeof bool); // 输出：boolean

// 定义 null 类型
let n = null;
console.log(typeof n); // 输出：object

// 定义 undefined 类型
let u;
console.log(typeof u); // 输出：undefined

// 定义对象类型
let obj = {
  name: "Tom",
  age: 18
};
console.log(typeof obj); // 输出：object

// 定义数组类型
let arr = [1, 2, 3, 4, 5];
console.log(typeof arr); // 输出：object

// 定义一个函数
function add(x, y) {
  return x + y;
}
// 调用函数
let result = add(1, 2);
console.log(result); // 输出 3