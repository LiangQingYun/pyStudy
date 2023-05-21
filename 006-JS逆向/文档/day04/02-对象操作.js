
var user = {}
user.name = '娜娜'
// console.log(user)

// Object.defineProperty(obj, prop, descriptor)
Object.defineProperty(user,'name',{
    value:'莹莹'
})

// console.log(user);

// 拦截JS对象里面的属性？  document cookie  拦截以后能下 debuger?
/*
*  找加密的位置
*    先定位设置的参数的位置  往上找堆栈  就可以排查到cookie加密的位置
*
* */

var names = '莉莉'
Object.defineProperty(user,'count',{
    get:function (){
      return   names
    },
    set:function (val){
        debugger;
        console.log('找到设置值的位置')
        names = val
    }
})
console.log(user.count);
user.count = '菲菲'
console.log(user.count)


// 赋值  添加数据的时候
Object.defineProperty(document,'cookie',{
    set:function (val){
        debugger;
        console.log('Hook捕获到cookie设置->', val);
        return val;
    }
})




