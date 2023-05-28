# -*- coding: utf-8 -*-

import json
import hmac
import hashlib

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

def _hmacSha512(v,k):
    return hmac.new(k.encode(), v.encode(), hashlib.sha512).hexdigest()

def s(v, e={}):
    t = v.lower()
    n = json.dumps(e).lower()
    key = r(t)
    hash_value = _hmacSha512((t + n), key).lower()
    return hash_value[8:28]

def r(e="/"):
    t = e.lower() * 2
    codes = _ps["codes"]
    ps_n = _ps["n"]
    result = ""
    for i in range(len(t)):
        a = ord(t[i]) % ps_n
        result += codes[str(a)]
    return result

print(s(path))