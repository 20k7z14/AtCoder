import sys
import os
f = open('test.txt','r')
sys.stdin = f

a = list(map(int,input().split()))
if a.count(5)==2 and a.count(7)==1:
    print('YES')
else:
    print('NO')
