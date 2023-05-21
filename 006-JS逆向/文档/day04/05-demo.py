# -*- coding: utf-8 -*-

import execjs

print(execjs.eval('Date.now()'))

js_code = '''
function xx(){
    return arguments
}
'''
res = execjs.compile(js_code).call('xx','123','123123',[1,2,3],{'name':'菲菲'})
print(res)


