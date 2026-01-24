import sys
input = sys.stdin.readline

MOD = 1000

def mat_mul(A, B, n):
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k] == 0:
                continue
            aik = A[i][k]
            for j in range(n):
                C[i][j] = (C[i][j] + aik * B[k][j]) % MOD
    return C

def mat_pow(A, b, n):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        result[i][i] = 1

    base = A

    while b > 0:
        if b % 2 == 1:
            result = mat_mul(result, base, n)
        base = mat_mul(base, base, n)  # 제곱
        b //= 2
    return result

n, b = map(int, input().split())
A = [list(map(lambda x: int(x) % MOD, input().split())) for _ in range(n)]

ans = mat_pow(A, b, n)
for row in ans:
    print(*row)