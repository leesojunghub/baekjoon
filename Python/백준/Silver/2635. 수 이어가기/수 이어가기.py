import sys

input = sys.stdin.readline
n = int(input())
best_len = 0
best_arr = []
for i in range(0, n+1):
    arr = [n, i]
    idx = 1
    while True:
        if arr[idx-1] - arr[idx] < 0:
            break
        else:
            arr.append(arr[idx-1] - arr[idx])
            idx += 1
    if len(arr) > best_len:
        best_len = len(arr)
        best_arr = arr.copy()
print(best_len)
print(" ".join(map(str, best_arr)))