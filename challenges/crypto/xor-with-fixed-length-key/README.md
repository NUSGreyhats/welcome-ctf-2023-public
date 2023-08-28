# Challenge Details

```python3
import os, random, hashlib
from itertools import cycle

pt   = [i%230 for i in os.urandom(500000)]
klen = random.randint(1000,10000)
key  = random.getrandbits(klen*8).to_bytes(klen, 'big')

open('ct', 'wb').write(bytes(c^i for c,i in zip(pt, cycle(key))))

flag = "greyhats{%s}"%hashlib.sha256(key).hexdigest()
print(flag)
```

# Author

JuliaPoo

# Setup Instructions

no setup

# Author

Jules

# Solution

Gotta go into MT19937 to get enough info to solve this. [solve.py](./solve.py)

# Learning Objectives

Insanity Check

Understading python random (MT19937) implementation
 
# Flag

greyhats{9db96ca272e09ca76491d8c2eebf1ea10b8940440c5833146b72c0db361e6236}
