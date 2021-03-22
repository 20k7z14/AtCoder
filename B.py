import sys
import os
f = open('test.txt','r')
sys.stdin = f

n = int(input())
point = []
for i in range(n):
    point.append(list(map(int,input().split())))

print(point)
