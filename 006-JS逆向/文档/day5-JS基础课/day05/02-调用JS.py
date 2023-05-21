# -*- coding: utf-8 -*-

import execjs
from loguru import logger
# pip install PyExecJS

# 对JS进行编译
with open('01-code.js', encoding='utf-8') as f:
    js_code = f.read()

cell = execjs.compile(js_code)

print('第一次输出--》',cell.call('xl'))
print('第二次输出--》',cell.call('xl'))
print('第三次输出--》',cell.call('xl'))

# pip install  py_mini_racer
from py_mini_racer import MiniRacer
ctx = MiniRacer()
ctx.eval(js_code)
print('第一次输出--》',ctx.call('xl'))
print('第二次输出--》',ctx.call('xl'))
print('第三次输出--》',ctx.call('xl'))

