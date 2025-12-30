import sys
month = [31,28,31,30,31,30,31,31,30,31,30,31]
day = {
    0: "SUN",
    1: "MON",
    2: "TUE",
    3: "WED",
    4: "THU",
    5: "FRI",
    6: "SAT"
}
x, y = map(int, sys.stdin.readline().split())
print(day[(sum(month[:x-1])+y)%7])