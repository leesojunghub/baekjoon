import sys
input = sys.stdin.readline

def fib(n):
    global cnt_1 
    if n == 1 or n == 2:
        cnt_1 += 1
        return 1  # 코드1
    else: 
        return (fib(n - 1) + fib(n - 2))
    
def fibonacci(n):
    global cnt_2
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        cnt_2 += 1
        f[i] = f[i - 1] + f[i - 2];  # 코드2
    return f[n]

n = int(input())
cnt_1 = 0
cnt_2 = 0
f = [0] * (n+1)
fib(n)
fibonacci(n)
print(cnt_1, cnt_2)