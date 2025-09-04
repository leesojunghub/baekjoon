import sys
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
for line in sys.stdin:
    line = line.strip()
    not_repeating, repeating = line.split('(')
    repeating = repeating.rstrip(')')
    integer_part, decimal_part = not_repeating.split('.')
    non_repeat = decimal_part
    full_decimal = decimal_part + repeating
    numerator = int(integer_part + full_decimal) - int(integer_part + decimal_part)
    denominator = (10 ** len(full_decimal)) - (10 ** len(decimal_part))
    r = gcd(numerator, denominator)
    numerator //= r
    denominator //= r
    print(f"{line} = {numerator} / {denominator}")