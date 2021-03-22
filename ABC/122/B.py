import sys
import os
f = open('test.txt','r')
sys.stdin = f

S = input()
T = ['A','C','G','T']
ans = 0
cnt = 0
for i in range(len(S)):
    if S[i] in T:
        cnt += 1
        ans = max(ans,cnt)
    else:
        cnt = 0
        ans = max(ans,cnt)
print(ans)
