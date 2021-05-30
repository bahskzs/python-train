import base64

"""
用于加密解密的demo
Created on 2021/05/07

@author : bahskzs

"""

#s = 'ZLRM2019@CDH5!16.2'

pwdStr=base64.b64encode(bytes("QAZwsx123", 'utf-8')).decode('ascii')
print(pwdStr)

#b'aGVsbG8sIHdvcmxk'

print(base64.b64decode("MTIzNDU2").decode('ascii'))

#b'hello, world'
