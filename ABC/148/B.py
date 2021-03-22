import sys
import os
f = open('test.txt','r')
sys.stdin = f

n = int(input())
s,t = map(str,input().split())
ans = ''
for x,y in zip(s,t):
    ans += x+y
print(ans)
