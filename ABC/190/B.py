import sys
import os
f = open('test.txt','r')
sys.stdin = f

N,S,D = map(int,input().split())
magic = [list(map(int,input().split())) for i in range(N)]

damage = []
for m in magic:
    if m[0] < S and m[1] > D:
        damage.append(True)
    else:
        damage.append(False)

if any(damage):
    print('Yes')
else:
    print('No')
