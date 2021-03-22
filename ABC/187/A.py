import sys
import os
f = open('test.txt','r')
sys.stdin = f

a,b = map(str,input().split())
A,B = [int(i) for i in a],[int(j) for j in b]

print(max(sum(A),sum(B)))
