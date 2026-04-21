import sys
input = sys.stdin.readline

def count_ones(n):
    if n < 0:
        return 0
    total = 0
    bit = 1
    while bit <= n:
        cycle = bit * 2
        full_cycles = (n + 1) // cycle
        total += full_cycles * bit
        remainder = (n + 1) % cycle
        total += max(0, remainder - bit)
        bit *= 2
    return total

a, b = map(int, input().split())
print(count_ones(b) - count_ones(a - 1))