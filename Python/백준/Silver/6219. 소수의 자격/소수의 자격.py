import sys
from math import isqrt

def primes_in_range(a: int, b: int) -> set[int]:
    if b < 2: 
        return set()
    L = max(a, 2)
    lim = isqrt(b)
    base = bytearray([1]) * (lim + 1)
    base[0:2] = b'\x00\x00'
    for p in range(2, isqrt(lim) + 1):
        if base[p]:
            base[p*p:lim+1:p] = b'\x00' * (((lim - p*p) // p) + 1)
    base_primes = [i for i in range(2, lim+1) if base[i]]

    seg = bytearray([1]) * (b - L + 1)
    for p in base_primes:
        start = max(p*p, ((L + p - 1)//p)*p)
        seg[start - L:b - L + 1:p] = b'\x00' * (((b - start)//p) + 1)

    return {L + i for i, v in enumerate(seg) if v}
a, b, d = map(int, sys.stdin.readline().split())
primes = primes_in_range(a, b)
c = sum(1 for x in primes if str(d) in str(x))
print(c)