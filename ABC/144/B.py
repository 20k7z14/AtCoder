import sys
import os
f = open('test.txt','r')
sys.stdin = f

def kuku(n):
    for i in range(1,10):
        for j in range(1,10):
            if n == i*j:
                return True
    return False

n = int(input())
if kuku(n):
    print('Yes')
else:
    print('No')
