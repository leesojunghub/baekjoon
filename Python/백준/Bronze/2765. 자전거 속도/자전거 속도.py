import sys
input = sys.stdin.readline

pi = 3.1415927
n = 1

while True:
    diameter, rotation, time = map(float, input().split())
    if rotation == 0:
        break
    diameter = diameter / (12 * 5280)
    time = time / (60 * 60)
    distance = pi * diameter * rotation
    MPH = distance / time
    print(f"Trip #{n}: {distance:.2f} {MPH:.2f}")
    n += 1