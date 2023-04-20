//  方式一  : 通过花括号进行定义
let person = {
  name: 'John',
  age: 30,
  address: {
    street: '123 Main St',
    city: 'Anytown',
    state: 'CA'
  },
  sayHello: function() {
    console.log('Hello, my name is ' + this.name);
  }
};
console.log(person);

// 方式二 : 通过构造函数进行定义
function Person(name, age) {
  this.name = name;
  this.age = age;
  this.sayHello = function() {
    console.log('Hello, my name is ' + this.name);
  }
}

let person1 = new Person('John', 30);
console.log(person1);