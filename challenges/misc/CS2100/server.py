#!/usr/local/bin/python

from StackVM import StackVM
import secrets

try:
    n = int(input("Number of lines: "))
except:
    exit()

program = [
    input().strip() for _ in range(n)
    ]

print("Received program",flush=True)

for _ in range(100):
    args = [secrets.randbits(32),secrets.randbits(32)]
    vm = StackVM()
    vm.run(program, args)
    result = vm.stack[-1]
    if result != args[0]*args[1]:
        break
else:
    with open("flag.txt","r") as f:
        print(f.read())