import sys
import os
f = open('test.txt','r')
sys.stdin = f

n = int(input())
S = input()
ans = ''
for s in S:
    if ord('A') <= ord(s)+n and ord(s)+n <= ord('Z'):
        ans += chr(ord(s)+n)
    else:
        ans += chr(ord(s)+n-26)
print(ans)
