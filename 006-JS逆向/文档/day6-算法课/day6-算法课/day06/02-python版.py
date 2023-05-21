# -*- coding: utf-8 -*-

import base64
import random
import time

API_KEY = "a2c903cc-b31e-4547-9299-b6d07b7631ab"

class XK:
    @staticmethod
    def comb(t, e):
        n = "{}|{}".format(t, e)
        return base64.b64encode(n.encode()).decode()

    @staticmethod
    def encryptTime(t):
        t += 1111111111111
        e = list(str(t))
        n = random.randint(0, 9)
        r = random.randint(0, 9)
        o = random.randint(0, 9)
        e += [str(n), str(r), str(o)]
        return "".join(e)

    @staticmethod
    def encryptApiKey():
        e = list(API_KEY)
        n = e[:8]
        e = e[8:] + n
        return "".join(e)

    @staticmethod
    def getApiKey():
        t = int(time.time() * 1000)
        e = XK.encryptApiKey()
        t = XK.encryptTime(t)
        return XK.comb(e, t)


print(XK.getApiKey())