import sys
import os
f = open('test.txt','r')
sys.stdin = f

z = 2 * pow(10,12)
a, k = map(int,input().split())

cnt = 0
if k > 0:
    while a < z:
        a += 1 + k * a
        cnt += 1
    print(cnt)
else:
    print(z-a)
