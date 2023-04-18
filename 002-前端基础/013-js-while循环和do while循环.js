// 定义一个数组
let arr = [1, 2, 3, 4, 5];

// 使用 while 循环遍历数组
let j = 0;
while(j < arr.length) {
  console.log(arr[j]);
  j++;
}

// 使用 do-while 循环遍历数组
let k = 0;
do {
  console.log(arr[k]);
  k++;
} while(k < arr.length);

// 定义一个对象
let obj = {name: 'Tom', age: 18, gender: 'male'};

// 使用 for...in 循环遍历对象
for(let key in obj) {
  console.log(key + ': ' + obj[key]);
}
