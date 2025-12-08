import sys
n = int(sys.stdin.readline())
MOD = 1000000007

def mat_mul(a, b):
    return [
        [
            (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD,
            (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD,
        ],
        [
            (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD,
            (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD,
        ],
    ]

def mat_pow(mat, n):
    if n == 1:
        return mat
    if n % 2 == 0:
        half = mat_pow(mat, n // 2)
        return mat_mul(half, half)
    else:
        return mat_mul(mat, mat_pow(mat, n - 1))

base = [
    [1, 1],
    [1, 0],
]

m = mat_pow(base, n)
fn = m[0][1]
print(fn % MOD)
