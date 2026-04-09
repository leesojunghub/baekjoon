A, B, C = input().split()

A = int(A)
B = int(B)

if int(C[-1]) % 2 == 0:
    print(A)
else:
    print(A ^ B)