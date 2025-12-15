import sys
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
n = int(sys.stdin.readline())
for i in range(1,n+1):
    a, b = map(int,sys.stdin.readline().split())
    max_gcd = gcd(a, b)
    min_lcm = int(a * b / max_gcd)
    print(min_lcm, max_gcd)