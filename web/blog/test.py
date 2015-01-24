__author__ = 'lee'
import hashlib
s ='helloworld'
print(len(hashlib.sha512(s).hexdigest()))

