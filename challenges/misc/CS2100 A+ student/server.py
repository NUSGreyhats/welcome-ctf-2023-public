#!/usr/local/bin/python

from StackVM import StackVM
import gmpy2
import secrets

def new_prime():
    while True:
        p = secrets.randbits(24)
        if gmpy2.is_prime(p):
            return p

def new_exp(p):
    while True:
        e = secrets.randbits(16)
        if gmpy2.gcd(e,p-1)==1:
            return e

try:
    n = int(input("Number of lines: "))
except:
    exit()

program = [
    input().strip() for _ in range(n)
    ]

print("Received program",flush=True)

for _ in range(10):
    p = new_prime()
    e = new_exp(p)
    g = 2
    args = [g,e,p]
    vm = StackVM()
    vm.run(program, args)
    result = vm.stack[-1]
    if result != pow(*args):
        break
else:
    with open("flag.txt","r") as f:
        print(f.read())