const NodeRSA = require('node-rsa');


function rsaEncrypt() {
    pubKey = new NodeRSA(publicKey,'pkcs8-public');
    var encryptedData = pubKey.encrypt(text, 'base64');
    return encryptedData
}

function rsaDecrypt() {
    priKey = new NodeRSA(privatekey,'pkcs8-private');
    var decryptedData = priKey.decrypt(encryptedData, 'utf8');
    return decryptedData
}


var key = new NodeRSA({b: 1024});                    //生成1024位秘钥
var publicKey = key.exportKey('pkcs8-public');    //导出公钥
var privatekey = key.exportKey('pkcs8-private');  //导出私钥
var text = "I love Python!"

var encryptedData = rsaEncrypt()
var decryptedData = rsaDecrypt()

console.log("私钥:\n", privatekey)
console.log("解密字符串: ", decryptedData)
console.log(encryptedData);
console.log(publicKey);




