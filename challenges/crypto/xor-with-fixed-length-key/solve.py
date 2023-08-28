import random, z3, hashlib
import numpy as np
from functools import reduce

ct = open('./dist/ct', 'rb').read()
cposk = [set([i^k for i in range(230)]) for k in range(0x100)]

# Compute possible key bytes assuming pt is uniformly random on [0,230) (kpos)
# Also computes the only possible key length (klen)
for klen in range(1000, 10000):
    for i in range(klen):
        rad = reduce(lambda x,y: x & y, [cposk[c] for c in ct[i::klen]])
        if len(rad) == 0: break
    else: break
kpos = [reduce(lambda x,y: x & y, [cposk[c] for c in ct[i::klen]]) for i in range(klen)]
print("Key Length:", klen)

# Verify that internal_state -> key is indeed a linear (not just affine) transform
# GF(2)^19936 -> GF(2)^(klen*8)
s = random.getstate()
new_s = (s[0], (*[0]*624, s[1][-1]), s[2])
random.setstate(new_s)
assert random.getrandbits(klen*8) == 0

# Compute matrix representation of the transform (prng) by sampling the transform
# at the 19936 basis vectors.
prng = []
f = f"0{klen*8}b"
for bidx in range(624*32):
    print(f"Transforming {bidx+1}/{624*32}th basis", end="\r")
    new_s = (s[0], (*[0 if i != bidx//32 else 1<<(bidx%32) for i in range(624)], s[1][-1]), s[2])
    random.setstate(new_s)
    r = random.getrandbits(klen*8)
    prng.append([*map(int, format(r, f))])
prng = np.array(prng, dtype=bool)
print("Transform internal_state -> key computed!")

# Use z3 to encode the constraints
sol = z3.Solver()
kz3 = [z3.BitVec('k%d'%i, 8) for i in range(klen)] # symbolic key
bv  = [z3.BitVec('b%d'%i, 1) for i in range(19968)] # symbolic mt19937 state

# Assert that the key must be contained in the possible keys computed
# earlier (kpos)
for ks,k in zip(kz3, kpos):
    sol.add(reduce(z3.Or, map(lambda x: x == ks, k)))
# Assert that the key must be an mt19937 output by equating the symbolic key (kz3)
# as the transform of the symbolic internal state (bv)
# The matrix representation (prng) is used here
for i,k in enumerate(kz3):
    r8 = [reduce(lambda x,y: x^y, [bv[x] for x in np.where(prng[:,8*i+j])[0]]) for j in range(8)]
    sol.add(k == reduce(z3.Concat, r8))
print("Encoded Constraints!")

# Solve the model!
assert sol.check() == z3.sat
print("Recovered internal state!")

# Recover the internal state (bv) and compute the key
bvrec = [sol.model()[i] for i in bv]
bvrec = [0 if i==None else i.as_long() for i in bvrec]
rec_s = (s[0], (*[reduce(lambda x,y: (x<<1)+y, bvrec[i*32:i*32+32][::-1]) for i in range(624)], s[1][-1]), s[2])
random.setstate(rec_s)
key = random.getrandbits(klen*8).to_bytes(klen, 'big')
flag = "greyhats{%s}"%hashlib.sha256(key).hexdigest()
print("Flag:", flag)