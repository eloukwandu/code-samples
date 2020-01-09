import hashlib
import sys

m = "hello world"
s = m.encode( "utf8", "strict")
d = hashlib.sha512(s).hexdigest()
k = sys.getsizeof(d)


def ascii():
    for c in range(0, 256):
        print (chr(c))

print()

e = len(d)

print(d, "\n", e, "\n", k)
ascii()
#print(len(hashlib.sha256(s).hexdigest()))
