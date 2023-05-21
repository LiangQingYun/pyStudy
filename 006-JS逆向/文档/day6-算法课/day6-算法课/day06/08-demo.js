
const CryptoJS = require('crypto-js')


function MD5Test() {
    n =  Date.now().toString()
    text = n + "9527" + n.substr(0, 6)
    return CryptoJS.MD5(text).toString()
}
console.log(MD5Test());

