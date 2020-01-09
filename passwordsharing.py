from Crypto.Protocol.SecretSharing import Shamir
from Crypto import Random
from Crypto.Random import get_random_bytes

text = 'hello world'

password = input("Type ascii")
print ("it is....")

for ch in text:
    print(ord(ch), end="")
    #print(str(ch), end='')

for k in password:
    d = []
    d.append(k)
    s = list(enumerate(d, start=0))
    iv = [ get_random_bytes(d) for x in range(2)]
    res = Shamir.split(2, 5, iv)
    #print (ord(k))
    print(res)
    #print(d[:])


