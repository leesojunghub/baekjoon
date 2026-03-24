import sys
input = sys.stdin.readline

vowels = "aeiou"

while True:
    s = input().strip()
    if s == "end":
        break

    has_vowel = False
    v_cnt = 0
    c_cnt = 0
    ok = True

    for i in range(len(s)):
        if s[i] in vowels:
            has_vowel = True
            v_cnt += 1
            c_cnt = 0
        else:
            c_cnt += 1
            v_cnt = 0

        if v_cnt == 3 or c_cnt == 3:
            ok = False
            break

        if i > 0 and s[i] == s[i-1]:
            if s[i] not in "eo":
                ok = False
                break

    if not has_vowel:
        ok = False

    if ok:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")