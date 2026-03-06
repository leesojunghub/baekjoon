import sys

keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

for line in sys.stdin:
    line = line.rstrip('\n')
    output = ''
    
    for i in line:
        if i == ' ':
            output += ' '
        else:
            output += keyboard[keyboard.index(i)-1]

    print(output)