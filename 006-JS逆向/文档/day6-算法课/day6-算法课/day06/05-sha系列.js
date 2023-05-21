
var CryptoJS = require('crypto-js')

function SHA1Encrypt() {
    var text = "I love python!"
    return CryptoJS.SHA256(text).toString()
}

console.log(SHA1Encrypt())



