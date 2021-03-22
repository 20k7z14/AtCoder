import sys
import os
f = open('test.txt','r')
sys.stdin = f

n = int(input())
word = [input() for i in range(n)]
used = []
tail = word[0][-1]
draw = True

for cnt,w in enumerate(word[1:]):
    used.append(w)
    if used.count(w) < 2:
        if tail == w[0]:
            continue
        else:
            if cnt % 2 == 0:
                print('WIN')
            else:
                print('LOSE')
            draw = False
            break
    else:
        if cnt % 2 == 0:
            print('WIN')
        else:
            print('LOSE')
        draw = False
        break

if draw:
    print('DRAW')
