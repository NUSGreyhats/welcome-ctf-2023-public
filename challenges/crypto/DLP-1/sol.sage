from pwn import *
from hashlib import shake_256

def decrypt(s, c):
    key = shake_256(str(s).encode()).digest(len(c))
    return bytes([i ^^ j for i, j in zip(key, c)])

r = remote("localhost", 9999)

p = factorial(320) + 1

r.sendline(str(p))
r.sendline(str(2))

r.recvuntil("output: ")
A = int(r.recvline().decode())

r.recvuntil("c: ")
c = bytes.fromhex(r.recvline().decode())

s = discrete_log(GF(p)(A), GF(p)(2))

print(decrypt(int(s), c))