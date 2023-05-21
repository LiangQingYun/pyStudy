location = {}
location.href = 'https://wangdoc.com'
function nn(){
    if (location.href.length >2) {
        return '正确的数据'
    }else {
        return  '错误的数据'
    }
}
console.log(nn());


// 语法结构
navigator = {
    userAgent : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
document = {
        cookie:'trc_cookie_storage=taboola%2520global%253Auser-id%3D8dfc9116-526f-4a3e-8e9f-8a1e311c7868-tuct9d27a56; Hm_lvt_5eec262881855af3dede6a71234571f6=1681880689,1684159600,1684330157; _gid=GA1.2.1827621445.1684330157; Hm_lpvt_5eec262881855af3dede6a71234571f6=1684330302; _ga_ETCV30HD2T=GS1.1.1684330157.10.1.1684330301.0.0.0; _ga=GA1.2.4095506.1676988229'
    }
window = {
    navigator:navigator,
    document: document
}

function ll(){
    if (document['cookie'] ){
          return '正确的数据'
    }else {
        return  '错误的数据'
    }
}

console.log(navigator.userAgent);
console.log(window.navigator['userAgent']);
console.log(window.document.cookie)
console.log(document.cookie);

console.log(ll());





