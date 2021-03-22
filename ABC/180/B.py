import sys
import os
f = open('test.txt','r')
sys.stdin = f


import math
n = int(input())
x = list(map(int,input().split()))

manhattan = sum([abs(i) for i in x])
euclid = math.sqrt(sum([pow(abs(j),2) for j in x]))
chebychef = max([abs(k) for k in x])

print(manhattan)
print(euclid)
print(chebychef)
