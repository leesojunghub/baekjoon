import sys
input = sys.stdin.readline

n = int(input())

print(bin((n ^ (-n)) & 0xFFFFFFFF).count('1'))