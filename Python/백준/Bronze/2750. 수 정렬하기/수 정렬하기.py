n = int(input())
l = [int(input()) for _ in range(n)]
l.sort()
print("\n".join(map(str, l)))