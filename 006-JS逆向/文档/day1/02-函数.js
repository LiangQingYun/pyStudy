

function xxs(){
    console.log('123')
}

function xxs1(a,b,c,d){
    console.log(a,typeof a)
    console.log(b,typeof b)
    console.log(arguments);
    return a  // 终止了
    e = 6
    console.log(e)
}

// xxs1({'name':'莹莹'},['1','2'],'3','4','5')

var lili =  function (a,b,c){
    console.log('hello world')
}
// lili()


!(function () {
  console.log("Hello World!1");
})();

var li;
!(function () {
   function lili (){
       console.log('123~')
   }
   li = lili
})();
console.log(li());



var car = {name:"xialuo", model:500, color:"white"};
console.log(car,typeof car)


person = new Object();
person.firstname="John";
person.lastname="Doe";
person.age=50;
console.log(person)
console.log(person.age);
console.log(person['age']);

console.log(person['age']);



var persons = {
    firstName: "xl",
    lastName : "lili",
    id : 5566,
    fullName : function()
	{
       return this.firstName + " " + this.lastName;
    }
};
console.log(persons.fullName())





obj = {a: 'Hello', b: 'World'}
console.log(obj,typeof obj)
obj1 = JSON.stringify(obj)
console.log(obj1,typeof obj1)

obj2 ='{"a":"Hello","b":"World"}'
obj2 = JSON.parse(obj2)
console.log(obj2,typeof obj2)












