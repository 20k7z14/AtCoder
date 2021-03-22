import sys
import os
f = open('test.txt','r')
sys.stdin = f

n = int(input())
cnt = 0

odd = [i for i in range(1,n+1) if i % 2 == 1]
for od in odd:
    cd = 0
    for i in range(1,od+1):
        if od % i == 0:
            cd += 1
    if cd == 8:
        cnt += 1

print(cnt)
