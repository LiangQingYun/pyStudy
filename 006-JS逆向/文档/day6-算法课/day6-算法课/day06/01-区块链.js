

// 先扣入口
//
// {
//          key: "getApiKey", // 方法名称
//                     value: function() {
//                         var t = (new Date).getTime()
//                           , e = this.encryptApiKey();
//                         return t = this.encryptTime(t),
//                         this.comb(e, t)
//                     }
//                 }

// getApiKey = function() {
//     var t = (new Date).getTime()
//       , e = this.encryptApiKey();
//     return t = this.encryptTime(t),
//     this.comb(e, t)
// }
//
// function getApiKey() {
//     var t = (new Date).getTime()
//       , e = this.encryptApiKey();
//     return t = this.encryptTime(t),
//     this.comb(e, t)
// }

var API_KEY = "a2c903cc-b31e-4547-9299-b6d07b7631ab"
_xk = {
    comb:function(t, e) {
                        var n = "".concat(t, "|").concat(e);
                        return btoa(n)
                    },
    // "2795609717856485"
    encryptTime:function(t) {
            var e = (1 * t + 1111111111111).toString().split("")
              , n = parseInt(10 * Math.random(), 10)
              , r = parseInt(10 * Math.random(), 10)
              , o = parseInt(10 * Math.random(), 10);
            return e.concat([n, r, o]).join("")
      },
    // "-b31e-4547-9299-b6d07b7631aba2c903cc"
    encryptApiKey:function() {
                        var t = API_KEY
                          , e = t.split("")
                          , n = e.splice(0, 8);
                        return t = e.concat(n).join("")
                    },

    getApiKey:  function() {
        var t = (new Date).getTime()
          , e = this.encryptApiKey();
        return t = this.encryptTime(t),
        this.comb(e, t)
        }
}




