#!/usr/local/bin/python

from Crypto.Util.number import isPrime
from secrets import randbits
from hashlib import shake_256

FLAG = b'REDACTED'

def checkModulus(p):
    if not isPrime(p):
        print("Your modulus is not prime!")
        exit(0)

def encryptFlag(s):
    key = shake_256(str(s).encode()).digest(len(FLAG))
    return bytes([i ^ j for i, j in zip(key, FLAG)])

print("Let's perform Diffie–Hellman Key exchange!")
p = int(input("Send me your modulus: "))
g = int(input("Send me your base: "))

checkModulus(p)

secret = randbits(1024)
A = pow(g, secret, p)
print(f"My public output: {A}")
print(f"c: {encryptFlag(secret).hex()}")
