import sys
input = sys.stdin.readline

num = 1
while True:
    a, op, b = input().strip().split()
    a = int(a)
    b = int(b)
    match op:
        case ">":
            print(f"Case {num}: {str(a > b).lower()}")
        case ">=":
            print(f"Case {num}: {str(a >= b).lower()}")
        case "<":
            print(f"Case {num}: {str(a < b).lower()}")
        case "<=":
            print(f"Case {num}: {str(a <= b).lower()}")
        case "==":
            print(f"Case {num}: {str(a == b).lower()}")
        case "!=":
            print(f"Case {num}: {str(a != b).lower()}")
        case "E":
            break
    num += 1