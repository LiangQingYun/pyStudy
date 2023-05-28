const CryptoJS = require('crypto-js')

path = "/api/datalist/branchelist?keyno=9cce0780ab7644008b73bc2120479d31&nodename=branches&pageindex=1&sortfield=shoulddate"

_ps = {
    "n": 20,
    "codes": {
        "0": "W",
        "1": "l",
        "2": "k",
        "3": "B",
        "4": "Q",
        "5": "g",
        "6": "f",
        "7": "i",
        "8": "i",
        "9": "r",
        "10": "v",
        "11": "6",
        "12": "A",
        "13": "K",
        "14": "N",
        "15": "k",
        "16": "4",
        "17": "L",
        "18": "1",
        "19": "8"
    }
}


function _hmacSha512(v,k){
   return  CryptoJS.HmacSHA512(v,k).toString()
}

var s = function() {
        var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
          , t = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
          , n = JSON.stringify(e).toLowerCase();
        return _hmacSha512(t + n,r(t)).toLowerCase().substr(8, 20)
    };

var r = function() {
        for (var e = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase(), t = e + e, n = "", i = 0; i < t.length; ++i) {
            var a = t[i].charCodeAt() % _ps.n;
            n += _ps.codes[a]
        }
        return n
    };


console.log(s(path, undefined));




