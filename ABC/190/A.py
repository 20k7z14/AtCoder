import sys
import os
f = open('test.txt','r')
sys.stdin = f

a,b,c = map(int,input().split())

if c == 0:
    if a - b > 0:
        print('Takahashi')
    else:
        print('Aoki')

else:
    if b - a > 0:
        print('Aoki')
    else:
        print('Takahashi')
