import sys
import os
f = open('test.txt','r')
sys.stdin = f

n = int(input())
ans = 10
for i in range(1,(n+1)//2):
    if n%i==0:
        ans = min(ans,max(len(str(i)),len(str(n//i))))
print(ans)
