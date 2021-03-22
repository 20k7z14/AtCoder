import sys
import os
f = open('test.txt','r')
sys.stdin = f

n,m = map(int,input().split())
K,S = [],[]
for i in range(m):
    k,*s = map(int,input().split())
    K.append(k)
    S.append(s)

P = list(map(int,input().split()))

ans = 0
for bit in range(1 << n):
    flag = True
    for j in range(m):
        ons = 0
        for k in range(K[j]):
            if bit & 1 << (S[j][k] - 1):
                ons += 1
        if ons % 2 != P[j]:
            flag = False
    if flag:
        ans += 1
print(ans)
