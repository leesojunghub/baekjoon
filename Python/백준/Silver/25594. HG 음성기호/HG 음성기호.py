import sys
input = sys.stdin.readline

reverse_map = {
    'aespa': 'a',
    'baekjoon': 'b',
    'cau': 'c',
    'debug': 'd',
    'edge': 'e',
    'firefox': 'f',
    'golang': 'g',
    'haegang': 'h',
    'iu': 'i',
    'java': 'j',
    'kotlin': 'k',
    'lol': 'l',
    'mips': 'm',
    'null': 'n',
    'os': 'o',
    'python': 'p',
    'query': 'q',
    'roka': 'r',
    'solvedac': 's',
    'tod': 't',
    'unix': 'u',
    'virus': 'v',
    'whale': 'w',
    'xcode': 'x',
    'yahoo': 'y',
    'zebra': 'z'
}

s = input().strip()
i = 0
result = []

while i < len(s):
    matched = False
    
    for length in range(10, 1, -1):  
        if i + length <= len(s):
            word = s[i:i+length]
            if word in reverse_map:
                result.append(reverse_map[word])
                i += length
                matched = True
                break
    
    if not matched:
        print("ERROR!")
        exit()

print("It's HG!")
print(''.join(result))