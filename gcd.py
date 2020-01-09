def gcd(a, b):
        while b != 0:
            Remainder = a % b
            a = b
            b = Remainder

        return a

f = gcd(9, 3)
print(f)






