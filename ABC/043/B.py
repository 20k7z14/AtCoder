import sys
import os
f = open('test.txt','r')
sys.stdin = f

cmd = list(input())
word = []

for i in cmd:
    if i != 'B':
        word.append(i)
    else:
        if word != []:
            word.pop(-1)
        else:
            pass

print(''.join(word))
