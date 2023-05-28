const  JSEncrypt = require('jsencrypt');
const CryptoJS = require('crypto-js')


function get_pwd(pub,pub_code,pwd){
    var encrypt = new JSEncrypt ();
    encrypt.setPublicKey(pub);
    var encrypted = encrypt.encrypt(pub_code + CryptoJS.SHA512(pwd.toString()).toString());
    return encrypted
}




